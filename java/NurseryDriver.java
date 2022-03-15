/* NurseryDriver, Inventory, and Supplier are more projects assigned to me as part of a practical Java course
for incoming students to the VT-MIT program. They are designed to demonstrate more advanced knowledge of Java
methods, classes, and understanding of "is-a" and "has-a" relationships. */

import java.util.Scanner;

public class NurseryDriver {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);

		System.out.println("What is the supplier ID?");
		int supplierID = scan.nextInt();

		System.out.println("What is the supplier's name?");
		scan.nextLine();
		String supplierName = scan.nextLine();

		System.out.println("What is the supplier's phone number?");

		String supplierPhone = scan.nextLine();

		Supplier mySupplier = new Supplier(supplierID, supplierName, supplierPhone);

		System.out.println("Let's get the items from this supplier. How many are there?");
		int numOfItems = scan.nextInt();

		for (int itemNumber = 1; itemNumber <= numOfItems; itemNumber++) {

			System.out.println("What is the nursery item's name for item number " + itemNumber);

			scan.nextLine();
			String itemName = scan.nextLine();

			System.out.println("How many are in stock?");

			int numStock = scan.nextInt();

			System.out.println("How much does each item cost?");

			double itemPrice = scan.nextDouble();

			Inventory myInventory = new Inventory(itemName, numStock, itemPrice, mySupplier);

			System.out.println(myInventory.toString());
		}

	}

}
