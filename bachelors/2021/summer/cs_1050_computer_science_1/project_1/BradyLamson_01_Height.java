import java.util.Scanner;
import java.text.DecimalFormat;

public class BradyLamson_01_Height  {
  public static void main(String[] args) {
      // Convert a height entered in feet and inches into meters. 
      // input will be feet and inches
      // output should be in meters
      
      // Variable declarations --------------------------
      Scanner scan = new Scanner(System.in);
      int feet = 0;  // # of feet entered by the user
      int inches = 0; // # of inches entered by user
      
      // Input -------------------------------------------
      // Prompts user for height in feet and set that value to variable "feet"      
      System.out.println("Please input a positive integer in feet. (0 to exit):");
      feet = scan.nextInt();
      
      // Program exits if user inputs value equal to or less than 0
      if (feet <= 0)
      {
         System.exit(0);
      }
      
      // Promps user for height in inches and sets that value to variable "inches"
      System.out.println("Please input a positive integer in inches. (0 to exit):");
      inches = scan.nextInt();
      
      // Program exits if user inputs value less than 0
      if (inches < 0)
      {
         System.exit(0);
      }
      
      // Process ---------------------------------------
      // Calculate total inches by converting feet to inches and adding that to given inches.
      int totalInches = (feet * 12) + inches; 
      
      // Printing out a message for input greater than or equal to 8'. 
      if (totalInches >= 96)
      {
         System.out.println("Wow, you're super tall!");
      }
      
      // Convert totalInches to centimeters. Note: 2.54 centimeters per inch
      double totalCent = totalInches * 2.54;
      
      // Convert the centimeters to meters and centimeters, rounding to two places. 
      double totalMeters = totalCent / 100;
      
      // Allows for rounding to two decimal places. 
      DecimalFormat roundTwo = new DecimalFormat("#.##");
      
      // Output -----------------------------------------      
      // Print output and format it nicely. 
      System.out.println("Your height is " + feet + "'" + inches + "\"");
      System.out.println("Your height is " + roundTwo.format(totalMeters) + " meters or " + totalCent + " centimeters");  
      
      // Exit the program
      System.exit(0);
  }
}