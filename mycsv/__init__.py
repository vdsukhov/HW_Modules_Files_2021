import os.path as path


def read_csv(path_to_csv_file: str, delimiter=","):
    result = []
    abs_path = path.abspath(path_to_csv_file)
    try:
        with open(abs_path) as f:
            input_lines = [line.strip() for line in f]
        for line in input_lines:
            data_list = line.split(delimiter)
            length = len(data_list)
            count = 0
            while count < length:
                x = data_list[count].startswith('"')
                y = data_list[count].endswith('"')
                if x and not y:
                    count_int = 0
                    while True:
                        z = data_list[count + 1].endswith('"')
                        data_list[count] = data_list[count] + str(delimiter) + data_list[count + 1]
                        data_list.pop(count + 1)
                        count_int += 1
                        length -= count_int
                        if z:
                            data_list[count] = data_list[count][1:-1]
                            break
                elif x and y and data_list[count].find(".") != -1:
                    data_list[count] = data_list[count][1:-1]
                count += 1
            result.append(data_list)
    except FileNotFoundError:
        print("Error, such file doesn't exist")
    return result


def write_csv(path_to_csv_file: str, data: list[list], delimiter=',') -> None:
    if not isinstance(path_to_csv_file, str):
        print("Error, path to the file should be a string")
        return
    if not isinstance(data, list):
        print("Error, type of data variable should be a list of lists")
        return
    if not isinstance(delimiter, str):
        print("Error, delimiter should be a string")
        return
    abs_path = path.abspath(path_to_csv_file)
    output_list = []
    output_string = ""
    for i in range(len(data)):
        if not isinstance(data[i], list):
            print("Error, type of data variable should be a list of lists")
            return
        for j in range(len(data[i])):
            if not isinstance(data[i][j], str):
                print("Elements of list should be a string")
                return
            if data[i][j].find(delimiter) != -1 and j == len(data[i])-1:
                output_string = output_string + '"' + data[i][j] + '"' + "\n"
            elif data[i][j].find(delimiter) != -1 and j != len(data[i])-1:
                output_string = output_string + '"' + data[i][j] + '"' + delimiter
            elif delimiter == "," and data[i][j].find(".") != -1 and j == len(data[i])-1:
                output_string = output_string + '"' + data[i][j] + '"' + "\n"
            elif delimiter == "," and data[i][j].find(".") != -1 and j != len(data[i]) - 1:
                output_string = output_string + '"' + data[i][j] + '"' + delimiter
            elif data[i][j].find(delimiter) == -1 and j == len(data[i])-1:
                output_string = output_string + data[i][j] + "\n"
            else:
                output_string = output_string + data[i][j] + delimiter
        output_list.append(output_string)
        output_string = ""
    try:
        with open(abs_path, 'w') as ouf:
            for elem in output_list:
                ouf.write(elem)
    except FileNotFoundError:
        print("Error, such file or directory doesn't exist")
    except PermissionError:
        print("Error, access to directory or file is not permitted")
