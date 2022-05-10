[student name] [email]

CODE DESIGN AND DEVELOPMENT
The code asks for the name of the file that contains the data to be processed.
The code opens the files specified checks to ensure that the file exists and it it is readble otherwise appropriate error message is displayed and the code exits.
The code the reads the first line from the file and saves it to the variable n  as an integer while the the second line is saved to m.
The code the reads the second lines n*2 and parses the information in order to get appropriate women and their preferrences in the given order.
The code parses the information from above into a function called stable_match() in order to be processed.
A list of single men containingn the names of all the men is created.
in stable_match() function, checks if single_men list is empty. If it is not, it iterates through the names of the men on the list and passes thier name to a function called match().
The match() functions iterates through the preferrences of all women and assigns the current man a woman provided the woman is also single.
If a man gets a another proposal even if they have a partner then they either accept or reject the woman depending on thier preferrence.
After stability is obatined, all the matches are saved as lists in matched_couples list.
The code then continues to read from the file. It gets the the matches pre-recorded and uses the check_stability function to check if they are stable.
check_stability() function accepts 2 arguments, the candidate matches and the stable matches. For each candidate match, the code iterates through the stable_match list to check if the match is there, if it is not is stops execution otherwise it continues for n-1 times since if those match then the last one abviously will match.
The function returns the number of couples it had to go through in order to ascertain stability as well 0 is the matches are stable and 1 otherwise.
This information is stored in matches_result list as lists and later passed to save_output function in order to write the data to an external file.

USAGE
Just run the code using python3 and you will get prompted for a file name.
Enter the name of the file to be processed and check for the results in an output file shown by the program.