# Data-Analysis-Basketball-Stats-Tool

## Basketball Stats Tool rewritten for Data Analysis Track

I started the Team Teamhouse Data Analysis track and had to do a project similar to the original Basketball Stats tool I did. 
However, instead of just making the needed changes and submitting the project, I wanted to take the time to re-write the program to showcase my
better understanding of Python. 

This program imports players and their information, assigning the players to one of 3 teams. 
The program first has to 'scrub' some of the imported data so that Python can work with the data. 
The program then assigns the players to a team. 

When the user selects to display a team, the program will display the team name and the players in the team. 
In addition, the program sorts the players in height from shortest to tallest. It shows additional information such as a count 
of the experienced and inexperienced players, average height, and the guardians of the players. 

## How To Run

I wrote this program for Python 3.0 and higher. Unfortunately, my program has a function that Python 2.x cannot run. 

Download the files and open the terminal. Then, go to the folder contents and run the following:
 ```python
python app.py
```

## Program Preview

### Main Menu

Upon using this program, a main menu will greet you. Two options are available: Enter A to view a team's stats or B to exit the program. 

Entering A will bring you to another menu to input the corresponding letter of the team you wish to view. 

#### Example
Welcome To Cody's Basketball Tools!

Please enter the letter of the action
you want to perform.
Enter A for Team Stats
Enter B to exit the program
Enter Command:


#### Team sub-menu

Please Enter the Letter of the Team you want to view.
A) Panthers
B) Bandits
C) Warriors
D) Quit

#### Output

For this example, let us see the Panther's stats. Entering A will output the following:

=-=-= Team Name: Team Panthers =-=-=

Total Players: 6
Total Experienced: 3
Total Inexperienced: 3
Average Height: 42.17

* Arranged Shortest to Tallest: *
Players: Joe Kavalier, Matt Gill, Karl Saygan, Les Clay, Herschel Krustofski, Eva Gordon
Guardians: Sam Kavalier, Elaine Kavalier, Charles Gill, Sylvia Gill, Heather Bledsoe, Wynonna Brown, Hyman Krustofski, Rachel Krustofski, Wendy Martin, Mike Gordon

Press Enter to Return to Menu...

#### Exiting
Entering will return you to the team sub-menu. You can also exit the program from that sub-menu. 

### Thank you for viewing. Please reach out to me for any suggestions, questions, or comments. 

##### uppdated 12/2023
