/*
    Author: Brady Lamson
    Date: FILL THIS IN BEFORE SUBMISSION*******
    BradyLamson_03_Grocery does whatever it needs to do
    Project #3
    IDE: IntelliJ IDEA 2021.1.2 (Community Edition)
    Vocabulary Word:
    Inspirational Quote:
 */

// Imports ********************************************************************
import java.text.DecimalFormat;
import java.util.Scanner;
import java.util.ArrayList;

// Primary project class ******************************************************
public class BradyLamson_03_Grocery {
    // Instance variables -----------------------------------------------------
    private final Scanner scan = new Scanner(System.in);    // Access keyboard
    private static int groceryCount;
    private static ArrayList<GroceryListItem> groceryList = new ArrayList<>();
        // Creates list that holds grocery items. Makes input far less
        // prone to error than using multiple arrays.
    // groceryInput method ----------------------------------------------------
    public void groceryInput() {
        while(true) {
            // Variables local to the while loop ------------------------------
            GroceryListItem groceryItem = new GroceryListItem();
            String yesOrNo;
            // end loop variables ---------------------------------------------

            // Lines 63 -> 96 take in info on grocery item attributes
            System.out.print("\nPlease input a grocery item name or "
                    + "\npress <Enter> to exit the program: ");
            groceryItem.setItemName(scan.nextLine());

            // Exits loop when <Enter> is input at itemName step.
            if (groceryItem.getItemName().equals("")) {
                break;
            } // end if

            System.out.print("\nPlease input an item price. ");
            // Below code tests to see if a number has been input or not.
            if(scan.hasNextDouble()) {
                groceryItem.setPrice(scan.nextDouble());
            } // end if
            else {
                System.out.println("Please input a valid number.");
                System.exit(0);
            } // end else

            System.out.print("Is the item on sale? yes or no: ");
            yesOrNo = scan.next().toLowerCase();

            switch (yesOrNo) {
                case "yes":     // Stacking cases allows for different
                case "y":       // cases to do the same thing. Like an 'or'.
                    groceryItem.setOnSale(true);
                    break;
                case "no":
                case "n":
                    groceryItem.setOnSale(false);
                    break;
                default:
                    System.out.print("Please input a valid character.");
                    System.exit(0);
            } // end switch

            // This nextLine resets the scanner and prevents a bug that causes
            // the loop to exit prematurely.
            scan.nextLine();

            groceryList.add(groceryItem); // Adds new grocery item to array
            groceryCount++;
        } // end while
    } // end groceryInput

    // printReport method -----------------------------------------------------
    public void printGroceryList(double taxRate, double discount) {
        // Note: I use taxRate and discount as parameters to allow for
        //       easy changes to them assuming the user wants different values.
        //       I thought this would be a neat feature to have.
        // method variables ---------------------------------------------------
        double subTotal = 0;                // Total price of groceries.
        double salePrice = 1 - discount;    // Gives percent for price on sale
        double tax;                         // Used to calculate tax
        DecimalFormat formatter = new DecimalFormat("#.00");

        // Make sure parameters can't pass in values that break the program.
        if (taxRate < 0 || discount < 0 || discount > 1) {
            System.out.println("Please input valid " +
                    "values for printGroceryList() parameters.");
            System.exit(0);
        }

        System.out.println("\nGrocery Bill\n"
                + "\nPurchases");
        // Enhanced for loop covered on page 437 of Java for dummies.
        // This type of for loop allows access to elements without worrying
        // about index.
        for (GroceryListItem item : groceryList) {
            if(item.getOnSale()) {
                System.out.println(item.getItemName()
                        + ": $"
                        + formatter.format(item.getPrice())
                        + "   SALE: $"
                        + formatter.format(item.getPrice() * salePrice));
                subTotal += item.getPrice() * salePrice;
            } // end if
            else {
                System.out.println(item.getItemName()
                        + ": $"
                        + formatter.format(item.getPrice()));
                subTotal += item.getPrice();
            } // end else
        } // end for loop

        tax = subTotal * taxRate;
        System.out.printf("\nSubtotal: %1s%4.2f", "$", + subTotal);
        System.out.printf("\n7%% tax: %3s%4.2f", "$", + tax);
        System.out.printf("\nTotal: %4s%4.2f", "$", + subTotal + tax);
        System.out.println("\nYou purchased " + groceryCount + " items!");
    } // end printReport

    // main method ------------------------------------------------------------
    public static void main(String[] args) {
        BradyLamson_03_Grocery myList = new BradyLamson_03_Grocery();
        myList.groceryInput();
        myList.printGroceryList(0.07, 0.20);
    } // end main
}   // end BradyLamson_03_Grocery

// Grocery item class  ********************************************************
class GroceryListItem {
    // Instance Variables -----------------------------------------------------
    private boolean onSale;     // If item is on sale it gets a 20% discount
    private String itemName;    // Name of the object
    private double price;       // Price of the object

    // default constructor ----------------------------------------------------
    public GroceryListItem() {
        price = 0;
        itemName = "";
        onSale = false;
    } // End default constructor

    // Note: I have deliberately made the below methods 1-liners as I feel it
    //       makes the code far more readable.
    // getter methods ---------------------------------------------------------
    public double getPrice() {return this.price;}

    public String getItemName() {return this.itemName;}

    public boolean getOnSale() {return this.onSale;}

    // setter methods ---------------------------------------------------------
    public void setPrice(double price) {this.price = price;}

    public void setItemName(String itemName) {this.itemName = itemName;}

    public void setOnSale(boolean onSale) {this.onSale = onSale;}
}