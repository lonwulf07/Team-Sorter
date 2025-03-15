# Team-Sorter
A python program used to sort players into different teams based on their position.

Team_Sorter.py
This file uses a predefined list in the code itself to randomise players using the random module. A little bit more time consuming as editing the list every time takes up too much time in the code and not everyone may have access to the internals of the program.

Team_Sorter(Pandas).py
This file is similar but instead uses pandas library to read an excel file stored in the io folder of python in the local environment to generate a list to work upon it and sort the players using random module. You can edit the code to change the value in the head() call of reading pandas dataframe of a column depending on how many records of a column you want to work upon and convert it into a list to avoid duplication.

Team_Sheet.xlsx
The excel sheet that I was using to read the players data.
