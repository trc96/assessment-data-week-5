log_file = open("um-server-01.txt") #Creates a variable that is set to open the file and allow us to access the data in it.


def sales_reports(log_file): #Function declaration that takes in 'log_file' as a parameter.
    for line in log_file: #For...in loop that is looking at each line in the file that was created as a variable on line 1.
        line = line.rstrip() #Modifying the the data we pulled in using .rstrip() to remove any trailing characters per line.
        day = line[0:3] #Creates the day variable that is being told that it is a splice of the line variable starting at the 0 index and going till the 3 index.
        if day == "Mon": #Since each day is only three letters, this if statement is checking that if those three letters are "Tue", then do something.
            print(line) #This is printing the ling that meets the confition set on line 8.


sales_reports(log_file) #Calls the function declared on line 4 and passes that function the 'log_file' variable from line 1 to look for lines that are from "Tue".
