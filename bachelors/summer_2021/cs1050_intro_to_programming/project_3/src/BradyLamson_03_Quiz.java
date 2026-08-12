/*
    Author: Brady Lamson, Milah Thomas
    Date: FILL THIS IN BEFORE SUBMISSION*******
    BradyLamson_03_Quiz does whatever it needs to do
    Project #3
    IDE: IntelliJ IDEA 2021.1.2 (Community Edition)
    Vocabulary Word:
    Inspirational Quote:
 */

// Imports ********************************************************************
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Scanner;

// Begin class BradyLamson_03_Quiz ********************************************
public class BradyLamson_03_Quiz    {
    // Instance variable declarations -----------------------------------------
    private int gradeCounter;           // Counts the number of quiz grades.
    private double runningTotal;        // The sum of all quiz grades
    private double average;             // Mean score of quiz grades
    private String userName;            // Name for the quiz report
    private String letterGrade;         // Letter grade for the average score
    private final Scanner scan = new Scanner(System.in);     // Access Keyboard
    private ArrayList<Double> gradeList = new ArrayList<>(); // List of grades

    // Default Constructor ----------------------------------------------------
    public BradyLamson_03_Quiz()    {
        gradeCounter = 0;
        runningTotal = 0;
        userName = "";
        letterGrade = "";
        average = 0;
    }   // End default Constructor

    // print intro method -----------------------------------------------------
    private static void printIntro() {
        // This prints out a simple introduction on how the program works.
        System.out.println(
                "\nThis program averages your quiz grades for you. \n"
                + "It even gives you an accurate letter grade! \n");
    }   // End printIntro method

    // scan name method -------------------------------------------------------
    private void scanName()    {
        // This method gets the name of the user.
        System.out.println("Please input your name, or press "
                + "<Enter> to exit the program. ");
        userName = scan.nextLine();

        // This allows the user to exit the program if they don't input a name.
        if (userName.equals("")) {System.exit(0);}
    }   // End scanName method

    // get quiz grade method --------------------------------------------------
    private void getQuizGrades() {
        System.out.println("Please input up to nine quiz grades or"
                + "\ninput '-1' to finish early: ");
        /*
            This loop takes quiz grades and saves them in an easily
            accessible list. This streamlines later aspects of the program!
            If a grade less than 0 is added it exits the loop and moves on.
            gradeCounter keeps a running tally on how many grades are put in.
        */
        for (int count = 1; count < 10; count++)  {
            gradeList.add(scan.nextDouble());
            if (gradeList.get(count - 1) < 0) {break;}
            runningTotal += gradeList.get(count - 1);
            gradeCounter++;
        } // end for loop
    }

    // Assign letter grade method ---------------------------------------------
    private void assignLetterGrade()  {
        average = runningTotal / gradeCounter;
        /* Note: This could also be achieved using gradeList.size()
                 I used gradeCounter to keep my code to spec.
         ***************************************************************
          The below batch of statements assigns a letter grade to different
          average scores. It follows a traditional ten point grading scale.
        */
        if (this.average >= 90 && this.average <= 100) {letterGrade = "A";}
        else if (this.average >= 80 && this.average < 90) {letterGrade = "B";}
        else if (this.average >= 70 && this.average < 80) {letterGrade = "C";}
        else if (this.average >= 60 && this.average < 70) {letterGrade = "D";}
        else if (this.average < 60) {letterGrade = "F";}
    }   // End assignLetterGrade method

    // printReport method -----------------------------------------------------
    private void printReport() {
        // These formatters allow for 1 decimal place and 0 decimal
        // places, respectively.
        DecimalFormat oneDecimalFormatter = new DecimalFormat("#.0");
        DecimalFormat noDecimalFormatter = new DecimalFormat("#");

        // Prints out all of the grades one by one.
        System.out.println("\nQuiz Report for " + userName + "\n");
        for (int index = 0; index < gradeList.size() - 1; index++) {
            System.out.println("Quiz #"
                + (index+1) 
                + ": " 
                + noDecimalFormatter.format(gradeList.get(index)));
        }
        // Prints out the average grade and the corresponding letter grade.
        System.out.println("\nQuiz average: "
            + oneDecimalFormatter.format(average)
            + "%\n"
            + "Quiz grade: " + letterGrade);
    }

    // grade quizzes method ---------------------------------------------------
    public void gradeQuizzes() {
        // This method streamlines the use of this program. There is little
        // reason for the user to need any individual methods here.
        printIntro();
        scanName();
        getQuizGrades();
        assignLetterGrade();
        printReport();
    }   // end gradeQuizzes method

    // main method ------------------------------------------------------------
    public static void main(String[] args)  {
        BradyLamson_03_Quiz myQuiz = new BradyLamson_03_Quiz();
        myQuiz.gradeQuizzes();
    }   // End main
}   // End BradyLamson_03_Quiz (class)
