import java.util.Scanner;

public class BradyLamson_01_Chess {
   public static void main(String[] args) {
      /*
      Goal: Take user input of coordinates on a chess board and determine if said square is black or white.
      Step: 1: Take user input in via a scanner.
            2: Check validity of user input by comparing to premade strings.
            3: Take index of user input within premade strings and determine if index is even or odd.
            4: If both number and letter index is the same (both even, both odd):
                Print out that square is black.
            5: If number and letter index is different (one even, one odd):
                Print out that square is white.
            6: At the end terminate the program.      
      */
      
      // Variable declarations ---------------------------
      Scanner scan = new Scanner(System.in);
      String userInput;             // Generates string variable that will later be assigned to what is entered into the scanner.
      String letters = "abcdefgh";  // Generate string of acceptable letters.
      String numbers = "12345678";  // Generate string of acceptable numbers. 
                                    // Needs to be a string of numbers to make comparing to userInput easier.
      
      String userLetter;            // Will be assigned to the first value in userInput string
      String userNumber;            // Will be assigned to the second value in userInput string
      int letterIndex;              // Both index values will be utilized to determine even or odd.
      int numberIndex;              
      String letterEvenOrOdd;       // EvenOrOdd variables utilized to determine board color.
      String numberEvenOrOdd; 
      
      // Input --------------------------------------------
      System.out.println("Please input a lowcase letter between 'a' and 'h' \nfollowed by a positive integer between 1 and 8:");
      userInput = scan.nextLine();
      // I use substring in the code below to take out the desired indexed character within a string. 
      // Since userInput should always be "letter" "number" we can use this method.
      userLetter = userInput.substring(0,1);
      userNumber = userInput.substring(1);      
      
      /*
         The following code checks to make sure that BOTH the better and value entered are found within our stated acceptable ranges.
         I check for values I don't want to ensure the process fails as soon as possible.  
      */
      
      if (letters.contains(userLetter) != true || numbers.contains(userNumber) != true)
      {
         System.out.println("Please input information within provided range (a-h and 1-8)");
         System.exit(0);
      }
      
      
      // Process ------------------------------------------
      letterIndex = letters.indexOf(userLetter);   // Assigns the letters index in our string of letters to an integer variable.
      numberIndex = numbers.indexOf(userNumber);   // Assigns the numbers index in our string of numbers to an integer variable.
         
      if ((letterIndex + 1) % 2 == 0)              // +1 is used here due to java using 0 index. 
      {                                            // (variable % 2) is the classic way to determine even or odd for a value.
         letterEvenOrOdd = "Even";
      }
      else
      {
         letterEvenOrOdd = "Odd";
      }
      
      if ((numberIndex + 1) % 2 == 0)              // +1 is more obvious in utility here. Without it 1 would be even, 2 odd, so on so forth.
      {
         numberEvenOrOdd = "Even";
      }
      else
      {
         numberEvenOrOdd = "Odd";
      }      
      
      /*
         The below even or odd comparison is done based on the following observation:
         Looking at the board, a1 is black, b2 is black, c3 is black. a2 is white, b1 is white, c2 is white. What's the pattern?
         If we think of 'a' as an "odd" letter, then we see that when paired with an odd number the panel is black. 
         When paired with an even number you get white. This is the same for the other squares as well. 
         If both the letter and number are the same, as in even, for example, the result is black. If they're different, you get a white square.
      */
      
      // Output --------------------------------------------------
      if (letterEvenOrOdd.equals(numberEvenOrOdd))  // .equals used here to compare contents of strings. I don't trust == in this situation.
      {
         System.out.println("Square " + userInput + " is black."); 
      }
      else
      {
         System.out.println("Square " + userInput + " is white.");
      }
      
      // Terminate the program
      System.exit(0);
   }
}