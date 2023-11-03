# Donaldson Security Functional Areas and Capabilities Quick Reference Guide

## Systems Administration (SA)
- (SA-01) Bastion Hosts: Bastion hosts are used to secure access to internal systems, reducing the attack surface by controlling access through a single point. They play a crucial role in network security.

- (SA-02) Out-of-Band (OOB) Management: OOB management allows administrators to access and manage network devices independently from the production network, enhancing resilience and security.

- (SA-03) Network Isolation: Network isolation involves segmenting networks to minimize lateral movement of threats, making it a fundamental element of cybersecurity.

- (SA-04) Integrated Lights-Out (ILO), Keyboard Video Mouse (KVM), and power controls: These technologies enable remote management and control of servers, contributing to system security and availability.

- (SA-05) Virtualization and Storage Area Network (SAN) Management: Proper management of virtualization and SAN resources is essential for maintaining data integrity and confidentiality.

- (SA-06) Separation of administration from services: Isolating administrative functions from regular services helps reduce the risk of unauthorized access or attacks.

- (SA-07) Multi-factor authentication: MFA provides an additional layer of security, ensuring that only authorized users can access systems and data.

- (SA-08) Administrator Audit Trails: Audit trails capture and store administrative activities, which can be invaluable for post-incident analysis and compliance.

- (SA-09) Command logging and analytics: Monitoring and analyzing command execution can help detect and respond to security incidents and policy violations effectively.
## Network Security (NS)
- (NS-01) Switches and Routers: Secure configuration and management of switches and routers are fundamental for network security, preventing unauthorized access and traffic control.

- (NS-02) Software Defined Networking (SDN): SDN offers centralized network control, enhancing security through programmability and automation.

- (NS-03) Domain Name System (DNS) and Dynamic Host Configuration Protocol (DHCP): DNS and DHCP security is crucial for preventing DNS attacks and ensuring IP address allocation integrity.

- (NS-04) Network Time Protocol (NTP): Proper NTP configuration is essential for synchronized time across network devices, aiding in event correlation and security analysis.

- (NS-05) Network Service Management: Managing network services securely ensures availability and prevents vulnerabilities from being exploited.

- (NS-06) Firewall and Virtual Machine Firewall: Firewalls provide network security by filtering traffic, while virtual machine firewalls protect virtualized environments.

- (NS-07) Network Intrusion Detection / Network Intrusion Prevention System (IDS/IPS): IDS/IPS systems monitor and protect against network-based threats, including unauthorized access and malicious traffic.

- (NS-08) Wireless Networking: Securing wireless networks involves encryption, access controls, and intrusion detection to prevent unauthorized access.

- (NS-09) Packet Intercept and Capture: Packet capture tools assist in network troubleshooting, incident response, and monitoring for security threats.

- (NS-10) SSL Intercept: SSL interception enables inspection of encrypted traffic for potential security threats or policy violations.

- (NS-11) Network Access Control (NAC): NAC solutions enforce security policies, ensuring that only compliant devices can access the network.

- (NS-12) Virtual Private Networking (VPN) and Internet Protocol Security (IPSec): VPNs and IPSec are essential for secure remote access and data encryption.

- (NS-13) Network Traffic Analysis (NTA): NTA tools help identify suspicious network activity and potential security breaches.

- (NS-14) Network Data Analysis (NDA): Analyzing network data is crucial for detecting anomalies, intrusion attempts, and security incidents.
## Application Security (AS)
- (AS-01) E-mail Security: Email security measures protect against phishing, malware, and spam to prevent unauthorized access and data breaches.

- (AS-02) Webshell detection: Detecting and preventing webshells is essential for identifying malicious code and unauthorized access to web applications.

- (AS-03) Application Firewalls: Application firewalls filter and protect web applications from various threats, including SQL injection and cross-site scripting (XSS).

- (AS-04) Database Firewalls: Database firewalls safeguard sensitive data by monitoring and filtering database traffic.

- (AS-05) Forward Proxy and Web Filters: Forward proxies and web filters control access to websites and content, reducing the risk of malware and inappropriate browsing.

- (AS-06) Reverse Proxy: Reverse proxies enhance security by acting as an intermediary between users and web servers, providing additional layers of protection.

- (AS-07) Data Leakage Protection (DLP): DLP solutions prevent unauthorized data exfiltration and ensure data compliance.

- (AS-08) Secure Application and Database Software Development: Secure development practices minimize vulnerabilities and improve application and database security.

- (AS-09) Software Code Vulnerability Analysis: Analyzing code for vulnerabilities helps identify and remediate security issues, reducing the risk of exploitation.
## Endpoint, Server, and Device Security (ESDS)
- (ESDS-01) Local Administrator Privilege Restrictions: Restricting local administrator privileges reduces the risk of unauthorized system changes and malware infection.

- (ESDS-02) Computer Security and Logging Policies: Security and logging policies provide guidelines for secure system configurations and effective event monitoring.

- (ESDS-03) Endpoint and Media Encryption: Endpoint and media encryption protect sensitive data on devices and removable media from unauthorized access.

- (ESDS-04) Computer Access Controls: Access controls limit access to systems, ensuring only authorized users can interact with devices.

- (ESDS-05) Forensic Imaging Support for Investigations: Forensic imaging capabilities are essential for preserving and analyzing digital evidence during security investigations.

- (ESDS-06) Virtual Desktop / Thin Clients: Virtual desktops and thin clients enhance security by centralizing computing resources and reducing the attack surface.

- (ESDS-07) Mobile Device Management (MDM): MDM solutions manage and secure mobile devices, enforcing policies and protecting corporate data.

- (ESDS-08) Anti-Virus and Anti-Malware: Anti-virus and anti-malware tools detect and remove malicious software, safeguarding devices and servers.

- (ESDS-09) Application Allowlisting: Application allowlisting permits only trusted applications to run, preventing the execution of unauthorized or malicious software.

- (ESDS-10) In-Memory Malware Detection: In-memory malware detection identifies and prevents threats that reside in system memory.

- (ESDS-11) Host Firewall and Intrusion Detection: Host-based firewalls and intrusion detection systems protect servers and endpoints from network-based threats.

- (ESDS-12) "Gold Code" Software Images: Using validated "gold code" images ensures secure and consistent server and device deployments.

- (ESDS-13) Security Technical Implementation Guides (STIGs): STIGs provide security configuration guidelines for devices and servers to meet stringent security standards.

- (ESDS-14) Always-On Virtual Private Networking (VPN): Always-on VPNs maintain secure connections for remote devices, safeguarding communication and data.

- (ESDS-15) File Integrity and Change Monitoring: Monitoring file integrity and changes helps detect unauthorized modifications and potential security breaches.
## Identity, Authentication, and Access Management (IAAM)
- (IAAM-01) Identity Life Cycle Management: Managing the complete identity life cycle, including provisioning and deprovisioning, ensures only authorized users have access.

- (IAAM-02) Enterprise Directory: Enterprise directories centralize user and group information, facilitating access control and authentication.

- (IAAM-03) Multi-Factor Authentication: MFA adds an extra layer of security by requiring multiple authentication factors, reducing the risk of unauthorized access.

- (IAAM-04) Privilege Management and Access Control: Privilege management enforces granular access controls, restricting users to the necessary resources and actions.

- (IAAM-05) Identity and Access Audit Trail and Reporting: Logging and reporting of identity and access events aid in security monitoring, compliance, and incident response.

- (IAAM-06) Lightweight Directory Access Protocol (LDAP): LDAP is used for accessing and managing directory services, such as user and group information.

- (IAAM-07) Kerberos, RADIUS, 802.1x: Authentication protocols like Kerberos, RADIUS, and 802.1x enhance network security and access control.

- (IAAM-08) Federated Authentication: Federated authentication allows users to access multiple systems and services with a single set of credentials, improving user experience and security.

- (IAAM-09) Security Assertion Markup Language (SAML): SAML is a standard for exchanging authentication and authorization data between parties, enabling single sign-on and secure access.
