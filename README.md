
# E02a-Control-Structures

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.


Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
I expect the program to say greeting and then ask what our favorite color is without giving a response after that

  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
  The program said greeting and then asked what my favoirt color without providing a response afterward
  
  - What do you think the program did with what you typed in answer to the question?
It tool in my awnser but didnt have anything to do with it so it was dropped

- Open main02.py. Before running it, describe how this is different than main01.py.
It assings the input to a variable and then has a print after that

  - What do you think the color = input() will do?
  It will ask for a color and assing that to the variable

  - Run the program in the terminal and answer the question. Did the program do what you expected?
Yes it did

- Open main03.py. Before running it, describe how this is different than main02.py.
It is different because it has an if else statement

  - What is happening on lines 9–12?
it checks to see if the color is red andd if it is it prints correct otherwise it says try agian

  - Why are lines 10 and 12 indented?
They are there to catch any response other than red

  - Run the program and answer the question. What happens if you don’t capitalize Red?
  it will tell you sorry try again

  - What does this tell you about "color"?
the variable is case specific

- Open main04.py. Before running it, describe how this is different than main03.py.
This accounts for both versions of red, one capitalized and one not capitalized

  - What problem is this trying to solve?
That the variable is case sensitive

  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
it will print sorry try agg\ain

- Open main05.py. What do you expect line 9 to do?
I expect that that will make the string in color all lowercase

  - What problem is it trying to solve?
that there are different capitalization schemes

  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
It will print sorry try again

 - Open main06.py. How is line 9 different than in main05.py?
it has the strip function

   - What would you guess .strip() is doing?
removes all spaces

   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
if you misspell red in any way it will break

 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
It is trying to include the option of pink as a response

   - What is happening on line 12?
It is using an else if statement

   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
It is to continually run the program until you provide an awnser other than red

   - Why are lines 10–17 indented?
They are there in order to either print correct or continually ask you what their favorite color is 

   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
it would break becuase the variable is before the while loop and can never be redefined

   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)

 - Open main09.py. What is happening on line 13?
it is count as count plus 1 thus every time the program runs it adds one to count

   - What is the purpose of “count”?
in order to figure out how many time it took you to guess the color

   - What is happening on line 22?
Well line 21 is printing a string plus what ever number count was

   - Run the program.


 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).

 - *Extra credit:* open main11.py. What is happening on lines 6-11?
Well line 6 is a function taht has the input variable last_color. it contains a list of potential colors and will chose one randomly. However in order to make sure it doesnt give the same color twice in a row it will check and make sure that the color c is not hte same as the last color used. it will run through the while loop until they are differnt then return the color to the game in the main while loop

Commit your changes and push them back to the repository.
 
---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
