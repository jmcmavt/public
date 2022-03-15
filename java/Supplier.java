//final review complete

package jmcmahonmod4;

public class Supplier {
	
	private int supplierId;
	private String companyName;
	private String phone;
	
	public Supplier() 
	{
		
	}
	
	public Supplier(int sid, String cna, String pho)
	{
		supplierId = sid;
		companyName = cna;
		phone = pho;
		
	}
	
	public String toString()
	{
		return "Your item's supplier is " + companyName + " with the id of " + supplierId + 
				" and has a phone number of " + phone;
	}

	public int getSupplierId() {
		return supplierId;
	}

	public void setSupplierId(int supplierId) {
		this.supplierId = supplierId;
	}

	public String getCompanyName() {
		return companyName;
	}

	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}
		
}
