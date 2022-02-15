## Convert a file from one format to another.

## The first format will be the apache log format as defaulted in cpanel

## The second format will be a CSV with double quote delimiters that Excel can read

## This program created with the aid of Copilot

# Imports
import sys
import re


# Example of a line in the apache log format
# 63.141.251.189 - - [14/Feb/2022:07:11:15 -0500] "GET /wp-login.php HTTP/1.1" 200 1923 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53"




# Define a function that converts the apache log format to a CSV
def apache_to_csv(file_name):
    # Open the file
    file = open(file_name, 'r')

    # Create a new file
    new_file_name = file_name.replace('log', 'log.csv')
    new_file = open(new_file_name, 'w')
    new_file.write('ip,dash,dash2,datetime,request,response,size,referer,useragent\n')


    i = 0
    for line in file:
        #inc i
        i += 1
        # Split the line into a list

        # convert [ and ] to " in line
        line = line.replace('[', '"').replace(']', '"')

        # split line on spaces but consider quoted strings as one word
        line_list = [p for p in re.split("( |\\\".*?\\\"|'.*?')", line) if p.strip()]      

        # Write the list to the new file
        new_file.write(','.join(line_list) + '\n')
    # Close the input file
    file.close()

    #close the output file
    new_file.close()


    # print to stderr done how many lines i   
    print('Done converting {} lines'.format(i), file=sys.stderr)
        





## main so that this file can be imported as a module
if __name__ == '__main__':
    # call the apache_to_csv function using the first arg as the parameter
    apache_to_csv(sys.argv[1])
