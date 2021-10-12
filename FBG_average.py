'''
"Patient_FBG_2021.csv"
has FBG (fasting blood glucose) values
for 200 subjects across three years.

Write a program that finds
the average FBG for each year.
Your program should read in the file
and write out the answer to a ".txt".
You will also need to include at least
one function within your script.

Your output should look like this
(note that these are not the actual answers):

Average FBG for Year_1:    121
Average FBG for Year_2:    130
Average FBG for Year_3:    107

Please make sure to submit both your script
and the output .txt file to brightspace.


'''

def get_data(csvpath):
    # Read in and tidy up the csv:
    with open(csvpath, 'r') as f:
        # read from csv line by line
        # and rstrip (right end strip) to remove '\n' at the end of line
        lines = [line.rstrip() for line in f]
        # print(lines)
        data = [line.split(',') for line in lines]
        # print(data)
        return data

def clean_up(data):
    # Remove the header row from data list:
    data.pop(0)

    # Remove the first column (names):
    for element in data:
        element.pop(0)
    # print(data)

    # Convert strings to ints:
    data = [[int(item) for item in element] for element in data]
    # print(data)
    return data

def do_maths(data):
    # Calculate averages, round and convert to int:
    # From stackoverflow, shorturl.at/jtJNV
    averages = [sum(x)/len(x) for x in zip(*data)]
    averages = [int(element) for element in averages]
    # print(averages)
    return averages
   
def write_file(averages, txtpath):
    i = 0
    with open(txtpath, 'a+') as f:  # a+ for append/don't want to overwrite
        for i in range(3):
            output = 'Average FBG for Year_{}:\t{}\n'.format(i, averages[i])
            # print(output)
            f.write(output)
            i += 1

csvpath = '/home/dani/Documents/Patient_FBG_2021.csv'
txtpath = '/home/dani/Documents/averages.txt'

data = get_data(csvpath)
data = clean_up(data)
averages = do_maths(data)
write_file(averages, txtpath)

