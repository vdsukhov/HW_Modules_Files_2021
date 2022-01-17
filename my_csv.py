def read_csv(path_to_csv_file, delimiter=","):
    if delimiter == ",":
        delimiter = ", "
    my_list = []
    try:
        with open(path_to_csv_file, "r") as my_file:
            for line in my_file:
                line.strip
                my_list.append(line.split(delimiter))	
    except EOFError:
        print("Error, such file doesn't exist")
    return my_list

def write_csv(path_to_csv_file, data, delimiter=','):
	with open(path_to_csv_file, "w") as my_file:
		for i in data:
			my_file.write(i+'\n')
	return my_file