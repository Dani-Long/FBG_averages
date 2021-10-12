'''
NOTE: there are several 'print(data)' lines in the code.
      These are there to help the student I was tutoring, 
      so they would learn how to check their code as they go.
      I would triple-quote remaining code and just run up to
      the print line, so progress can be monitored (if print
      returns what is expected, carry on. If not, fix something).
      
      Feel free to delete those lines if you like.

Instructions for assignment:
"Patient_FBG_2021.csv" has FBG (fasting blood glucose) values 
for 200 subjects across three years.

Write a program that finds the average FBG for each year.
Your program should read in the file and write out the answer to a ".txt".
You will also need to include at least one function within your script.

Your output should look like this
(note that these are not the actual answers):

Average FBG for Year_1:    121
Average FBG for Year_2:    130
Average FBG for Year_3:    107

'''
# Remember to update your paths for your local environment
csvpath = '/add/path/to/csv/'
txtpath = '/file/will/be/created/here'

def get_data(csvpath):
    # Read in the csv:
    with open(csvpath, 'r') as f:
        # Read from csv line by line
        # and rstrip (right-end strip) to remove '\n' at the end of line
        lines = [line.rstrip() for line in f]
        # print(data)    # Should be a big list of a list of strings
        return data

def clean_up(data):  
    # Data is a list of strings, so split into a list of lists
    data = [line.split(',') for line in lines]
    # print(data)   
    # (Should be a list of lists, each element a list of separate strings)
    # Remove the header row from data list (first element in LoL)
    data.pop(0)

    # Remove the first column (names) from LoL
    for element in data:
        element.pop(0)
    # print(data)     # Now, the first element should just be data, not headers

    # Convert strings to ints so we can get averages
    data = [[int(item) for item in element] for element in data]
    # print(data)  # Each element in LoL should just be a list of 3 ints
    return data

def do_maths(data):
    # Calculate averages, round and convert resulting float to int:
    # From stackoverflow, shorturl.at/jtJNV
    averages = [sum(x)/len(x) for x in zip(*data)]
    averages = [int(element) for element in averages]
    # print(averages)    # Should be a list of 3 integers
    return averages
   
def write_file(averages, txtpath):
    i = 0
    with open(txtpath, 'a+') as f:  # a+ for append b/c don't want to overwrite
        for i in range(3):
            output = 'Average FBG for Year_{}:\t{}\n'.format(i, averages[i])
            # print(output)  # Will show you what's writing to .txt file
            f.write(output)
            i += 1

data = get_data(csvpath)
data = clean_up(data)
averages = do_maths(data)
write_file(averages, txtpath)

