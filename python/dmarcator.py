#!/usr/bin/env python3
print("dmarcator.py is a free tool offered by joseph mcmahon, 2026. https://joemac.io")
"""
dmarcator.py is a free tool offered by joseph mcmahon. https://joemac.io

Generate DNS records that lock down a parked (non-sending) domain:

  * Null MX   - domain accepts no mail (RFC 7505)
  * SPF       - no server may send for the domain (-all)
  * DMARC     - reject anything that fails (p=reject, sp=reject)

Usage:
  python parked_domain_dns.py                       # prompts for the domain
  python parked_domain_dns.py mycompany.net
  python parked_domain_dns.py a.net b.com --rua dmarc-reports@yourmaindomain.com
  python parked_domain_dns.py mycompany.net --zone -o mycompany.net.zone
"""

import argparse
import re
import sys

LABEL_RE = re.compile(r"^(?!-)[a-z0-9-]{1,63}(?<!-)$")
EMAIL_RE = re.compile(r"^[^@\s]+@([^@\s]+)$")


def normalize_domain(raw: str) -> str:
    """Clean up user input and validate it as a domain name."""
    d = raw.strip().lower()
    d = re.sub(r"^[a-z]+://", "", d)   # strip http:// etc.
    d = d.split("/")[0].rstrip(".")    # strip paths and trailing dot
    if not d:
        raise ValueError("empty domain")

    try:  # support internationalized names by converting to punycode
        d = d.encode("idna").decode("ascii")
    except UnicodeError:
        raise ValueError(f"'{raw}' is not a valid domain name")

    labels = d.split(".")
    if len(labels) < 2 or len(d) > 253 or not all(LABEL_RE.match(l) for l in labels):
        raise ValueError(f"'{raw}' is not a valid domain name")
    return d


def validate_rua(rua: str) -> tuple[str, str]:
    """Return (address, domain_of_address)."""
    rua = rua.strip().removeprefix("mailto:")
    m = EMAIL_RE.match(rua)
    if not m:
        raise ValueError(f"'{rua}' is not a valid email address")
    return rua, normalize_domain(m.group(1))


def is_same_org(domain: str, report_domain: str) -> bool:
    """True if the report address is on the domain itself or one of its subdomains."""
    return report_domain == domain or report_domain.endswith("." + domain)


def build_records(domain: str, rua: str | None, wildcard_spf: bool):
    """Return (records, authorization_record_or_None).

    records: list of (name, type, value) for the parked domain's zone.
    authorization: (name, type, value, zone) for the reporting domain's zone.
    """
    records = [
        ("@", "MX", "0 ."),
        ("@", "TXT", '"v=spf1 -all"'),
    ]
    if wildcard_spf:
        records.append(("*", "TXT", '"v=spf1 -all"'))

    dmarc = "v=DMARC1; p=reject; sp=reject"
    authorization = None
    if rua:
        address, report_domain = validate_rua(rua)
        dmarc += f"; rua=mailto:{address}"
        if not is_same_org(domain, report_domain):
            authorization = (
                f"{domain}._report._dmarc",
                "TXT",
                '"v=DMARC1"',
                report_domain,
            )
    records.append(("_dmarc", "TXT", f'"{dmarc}"'))
    return records, authorization


def render(domain, records, authorization, include_zone_header, serial):
    out = []
    out.append(f"; ===== Parked domain: {domain} =====")
    out.append(f"$ORIGIN {domain}.")
    out.append("$TTL 3600")
    out.append("")

    if include_zone_header:
        out += [
            "; --- Zone authority (PLACEHOLDERS: replace with your provider's values) ---",
            f"@       IN  SOA   ns1.example-dns.com. hostmaster.{domain}. (",
            f"                  {serial:<11} ; serial (YYYYMMDDNN)",
            "                  7200        ; refresh",
            "                  3600        ; retry",
            "                  1209600     ; expire",
            "                  3600 )      ; negative-caching TTL",
            "",
            "@       IN  NS    ns1.example-dns.com.",
            "@       IN  NS    ns2.example-dns.com.",
            "",
        ]

    comments = {
        ("@", "MX"): "; Null MX: domain accepts no mail (RFC 7505)",
        ("@", "TXT"): "; SPF: no server may send for this domain",
        ("*", "TXT"): "; SPF for subdomains (SPF is not inherited)",
        ("_dmarc", "TXT"): "; DMARC: reject failures, including subdomains",
    }
    for name, rtype, value in records:
        out.append(comments[(name, rtype)])
        out.append(f"{name:<7} IN  {rtype:<4} {value}")
        out.append("")

    if authorization:
        name, rtype, value, zone = authorization
        out.append(f"; ----- Add this to the zone for {zone} (the REPORT-RECEIVING domain) -----")
        out.append(f"; Authorizes {zone} to receive DMARC reports about {domain}.")
        out.append(f"; (Or publish one wildcard instead:  *._report._dmarc  IN  TXT  {value})")
        out.append(f"{name}.{zone}.  IN  {rtype}  {value}")
        out.append("")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description="Generate parked-domain SPF/DMARC/null-MX records.")
    p.add_argument("domains", nargs="*", help="one or more domains (prompts if omitted)")
    p.add_argument("--rua", help="mailbox for DMARC aggregate reports (optional)")
    p.add_argument("--no-wildcard", action="store_true",
                   help="skip the wildcard SPF record for subdomains")
    p.add_argument("--zone", action="store_true",
                   help="include placeholder SOA/NS records for a full zone file")
    p.add_argument("-o", "--output", help="write to this file instead of stdout")
    args = p.parse_args()

    raw_domains = args.domains
    if not raw_domains:
        entered = input("Enter domain(s), separated by spaces or commas: ")
        raw_domains = re.split(r"[,\s]+", entered.strip())
        raw_domains = [d for d in raw_domains if d]
    if not raw_domains:
        sys.exit("No domain provided.")

    from datetime import date
    serial = int(date.today().strftime("%Y%m%d") + "01")

    chunks, errors = [], []
    for raw in raw_domains:
        try:
            domain = normalize_domain(raw)
            records, auth = build_records(domain, args.rua, not args.no_wildcard)
            chunks.append(render(domain, records, auth, args.zone, serial))
        except ValueError as e:
            errors.append(str(e))

    for e in errors:
        print(f"Error: {e}", file=sys.stderr)
    if not chunks:
        sys.exit(1)

    result = "\n".join(chunks)
    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
        print(f"Wrote {len(chunks)} domain(s) to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
