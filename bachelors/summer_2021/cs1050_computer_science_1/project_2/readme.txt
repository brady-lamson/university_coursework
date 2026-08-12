The current breakdown in my code is pretty confusing, and is a different bug than it may seem on a regular run of the program. 

What appears to be the bug AT FIRST:
	Instructions print twice on the second loop. Explanation? Seemingly none. There is nothing in the code that would indicate a double print. What's happening?
	
What is ACTUALLY the issue (I think):
	Using the debugger and running through my code line by line in the calculate() method I noticed something weird.
	The first pass through the code is perfect, works as expected.
	The second pass though, it seems there's some issue with the assignment of userInput. The program seems to just pass over the line. 
	From here it TRIES to enter the if else statements, fails, and starts the loop again. 
	Then it starts the third loop, which runs into the same issue if you keep going. The report works fine at least. 
	
	What seems to be the instructions printing twice is ACTUALLY the program shitting its pants after the loop. I have no idea why this is occurring. 
