import os
import re

def create_regex(delimiter):
    # Python seems to have problems when using * and + inside regular expressions. These characters need to be escaped when creating the regular expression
    if delimiter == "+":
        delimiter_regex = "\+"
    elif delimiter == "*": 
        delimiter_regex = "\*"
    else: 
        delimiter_regex = delimiter
    regex = delimiter_regex + "(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"
    return regex


def read_csv(path_to_csv_file, delimiter=","):
    result =  list()
    if os.path.isfile(path_to_csv_file):
        with open(path_to_csv_file, 'r') as file_h:
            data = file_h.read()
            data_splitted_by_lines = data.split('\n') 
            for elem in data_splitted_by_lines: 
                # We need to treat anything between quotes as data and do not split it. For this we use split function from re module, and we split on regular expression.
                data_splitted_inside_lines = re.split(create_regex(delimiter), elem)
                result.append(data_splitted_inside_lines)
        return result 
    else: 
        print ("Error, such file doesn't exist")
        return [] 


def write_csv(path_to_csv_file, data, delimiter=","): 
    #test if the call is correct to the function
    if not(isinstance(path_to_csv_file, str)):
        print("You need to provide a string as a path for the csv_file")
        return
    if not(isinstance(data, list)): 
        print("You need to provide a list as data to write ")
        return 
    else: #a list is provided
        for elem in data: 
            if not(isinstance(elem, list)): 
                print("Every line should be a list")
                return 
    #write in file 
    with open(path_to_csv_file, 'w') as file_h:
        for elem in data: #This is one line 
            for word in elem:
                # Handle data containing the delimiter
                if delimiter in word: 
                    file_h.write('\"' + word + '\"')
                else:
                    file_h.write(word)
                if elem.index(word) != len(elem)-1: #do not put the delimiter at the end of line
                    file_h.write(delimiter)
            file_h.write('\n')
    return  




    

