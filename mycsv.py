import os

def read_csv(path_to_csv_file, delimiter=","):
    if not os.path.exists(path_to_csv_file):
        print("Error, such file doesn't exist")
        return list()

    def fancy_split(S, delimiter = ','):
        S += delimiter
        result_S = []
        string = ""
        flag = False
        for i in S:
            if i in ('"',"'"):
                flag = not flag
                continue
            if i == delimiter and not flag:
                result_S.append(string.strip())
                string = ""
            else:
                string += i
        return result_S

    my_list = []

    with open('data_1.csv') as inp_f:
        for line in inp_f:
            my_list.append(fancy_split(line, delimiter))
    return my_list

def write_csv(path_to_csv_file, data, delimiter=','):
    if not isinstance(data, list):
        print('Data is not a list')
        return
    try:
        if not isinstance(data[0], list):
            print('Data is not a 2D list')
            return
    except IndexError:
        print('Data is not a 2D list')
        return
    with open(path_to_csv_file, 'w') as f:
        new_data = []
        for line in data:
            new_line = []
            for value in line:
                if delimiter in value:
                    value = f'"{value}"'
                new_line.append(value)
            new_data.append(delimiter.join(new_line))
        f.writelines('\n'.join(new_data))

