/* EatEm is part of a project assigned to me in a practical Java course for incoming graduate students to the
Virginia Tech master's of information technology program. 

The program demonstrates several fundamental concepts related to Java and object-oriented programming,
 and has a fun theme of a Japanese vending machine selling dried, edible insects. 
 
 All code is my own. */

import java.util.Locale;
import java.util.Scanner;
import java.text.NumberFormat;

public class EatEm {

	public static void main(String[] args) {

		NumberFormat jp = NumberFormat.getCurrencyInstance(Locale.JAPAN);
		NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);

		Scanner scan = new Scanner(System.in);
		boolean validSnack = false;
		String more = "yes";

		String selection = " ";

		System.out.println("いらっしゃいませ！Welcome to BUGSNAX! Number one bug vending in Nihon!\n");

		while (more.equalsIgnoreCase("yes")) { //start of loop

			System.out.println("What kind of BUG would you like? Your options:");
			System.out.println("Cricket (CR) Meal Worm (MW) Locust (LO) Cicada (CI) Silk Worm (SW)\n");
			System.out.print("Enter your 2-letter SNAX code: ");

			selection = scan.nextLine();

			validSnack = valid(selection); // check to make sure selection is valid

			if (validSnack == false) {
				System.out.println("Not a valid SNAX code! Try again!");
				continue;
			}

			System.out.println("Your total is " + jp.format(cost(selection)));

			int balance = cost(selection);

			payBill(balance);

			double usd = convert(balance);
			System.out.println("In USD, your snack would've cost: " + us.format(usd));

			System.out.println("\n美味しい! Delicious! More snacks? (yes/no)");
			more = scan.nextLine();
		} // end of loop
	}

	public static boolean valid(String snackChoice) {
		if ((snackChoice.equalsIgnoreCase("CR") || snackChoice.equalsIgnoreCase("MW")
				|| snackChoice.equalsIgnoreCase("LO") || snackChoice.equalsIgnoreCase("CI")
				|| snackChoice.equalsIgnoreCase("SW"))) {
			return true;
		} else
			return false;
	}

	public static int cost(String snackCost) {
		int yourSnackCost = 0;
		if (snackCost.equalsIgnoreCase("CR"))
			yourSnackCost = 1480;
		if (snackCost.equalsIgnoreCase("MW"))
			yourSnackCost = 1580;
		if (snackCost.equalsIgnoreCase("LO"))
			yourSnackCost = 1680;
		if (snackCost.equalsIgnoreCase("CI"))
			yourSnackCost = 1380;
		if (snackCost.equalsIgnoreCase("SW"))
			yourSnackCost = 1480;
		return yourSnackCost;
	}

	public static void coinsBack(int coins) { // basically the same method used in coin class
		coins = -coins;
		int numFiveHundred = (coins / 500);
		coins = (coins % 500);
		int numOneHundred = (coins / 100);
		coins = (coins % 100);
		int numFifty = (coins / 50);
		coins = (coins % 50);
		int numTen = (coins / 10);
		coins = (coins % 10);

		System.out.println("You got " + numFiveHundred + " ￥500, " + numOneHundred + " ￥100, " + numFifty + " ￥50, and "
				+ numTen + " ￥10 coins back.");
	}

	public static void payBill(int bal) {
		NumberFormat jp = NumberFormat.getCurrencyInstance(Locale.JAPAN);
		int paid = 0;
		while (bal > 0) {
			paid = validCoin();
			bal = (bal - paid);
			if (bal < 0) {
				System.out.println("Your change is " + jp.format(Math.abs(bal)));
				// I borrowed the abs method from python, works here too
			} else {
				System.out.println("Your balance is " + jp.format(bal));
			}
		}

		if (bal == 0) {
			System.out.println("No change required! Itadakimasu!");
		} else if (bal < 0) {
			coinsBack(bal);
		}
	}

	public static int validCoin() {
		Scanner scan = new Scanner(System.in);
		int coin = 0;
		boolean validCoin = false;

		while (validCoin == false) {
			System.out.println("Deposit a coin - 10, 50, 100, or 500 ￥: ");
			coin = scan.nextInt();
			if (coin == 10 || coin == 50 || coin == 100 || coin == 500) {
				validCoin = true;
			} else {
				System.out.println("Invalid Coin!");
			}
		}
		return coin;
	}

	public static double convert(int yenToDollars) {
		int yen = yenToDollars;
		double dollars = 0;
		double convert = 110.0;
		dollars = ((yenToDollars * 1.0) / convert);
		return dollars;
	}
}
