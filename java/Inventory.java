//final review complete

package jmcmahonmod4;

import java.text.NumberFormat;

public class Inventory {
		
	private Supplier supplierInfo; // this wasn't in the UML diagram but I am pretty sure it's required here
	
	private int inventoryId;
	private String itemName;
	private int numInStock;
	private double priceEach;
	
	private static int nextNum = 1000;
	
	public Inventory()
	{
		inventoryId = nextNum;
		nextNum++;
	}
	
	public Inventory(String name, int stock, double price, Supplier sup)
	{
		itemName = name;
		numInStock = stock;
		priceEach = price;
		supplierInfo = sup;
		inventoryId = nextNum;
		nextNum++;
	}
	
	public String toString()
	{
		NumberFormat money =  NumberFormat.getCurrencyInstance();
		return itemName + " with id of " + inventoryId + " has " + numInStock + " in stock with a price each of "
				+ money.format(priceEach) + " and a total value of " + money.format(totalValue()) + "\n" + supplierInfo.toString();
		
	}
	
	public double totalValue()
	{
		double value = (numInStock * priceEach);
		return value;
	}

	public int getInventoryId() {
		return inventoryId;
	}

	public void setInventoryId(int inventoryId) {
		this.inventoryId = inventoryId;
	}

	public String getItemName() {
		return itemName;
	}

	public void setItemName(String itemName) {
		this.itemName = itemName;
	}

	public int getNumInStock() {
		return numInStock;
	}

	public void setNumInStock(int numInStock) {
		this.numInStock = numInStock;
	}

	public double getPriceEach() {
		return priceEach;
	}

	public void setPriceEach(double priceEach) {
		this.priceEach = priceEach;
	}

	public int getNextNum() {
		return nextNum;
	}

	public void setNextNum(int nextNum) {
		this.nextNum = nextNum;
	}
	
}
