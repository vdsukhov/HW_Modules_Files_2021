

def read_csv(csvPath, delimiter=","):
    data = []
    try:
        with open(csvPath, "r") as file:
            cou = 0
            quo = False
            if repr(delimiter)[1] == "\\" and repr(delimiter)[2] != "\\":
                delim2 = "\\t"
            else:
                delim2 = delimiter
            for row in file.readlines():
                if row != "\n":
                    data.append([])
                    for elem in row.strip().split(delim2):

                        if quo:
                            if len(elem) > 0:
                                if elem[-1] == '"':
                                    data[cou].append(mem + delimiter + elem[:-1])
                                    quo = False
                                else:
                                    mem += delimiter + elem
                            else:
                                mem += delimiter
                        else:
                            if elem[0] == '"':
                                if elem[-1] != '"' or len(elem) == 1:
                                    mem = elem[1:]
                                    quo = True
                                else:
                                    data[cou].append(elem[1:-1])
                            else:
                                data[cou].append(elem)
                cou += 1
    except FileNotFoundError:
        print("Error, such file doesn't exist")
    return data


def write_csv(filePath, data, delimiter=","):
    if type(filePath) != str:
        print('Error, incorrect file name, use: "MyFileName"')
        return
    elif type(delimiter) != str:
        print('Error, incorrect delimiter, it should be a string')
        return
    elif type(data) != list:
            print('Error, incorrect data format, it should be two dimensional list of strings')
            return
    else:
        for row in data:
            if type(row) != list:
                print('Error, incorrect data format, it should be two dimensional list of strings')
                return
            else:
                for elem in row:
                    if type(elem) != str:
                        print('Error, incorrect data format, values should be strings')
                        return

        with open(filePath, 'w') as file:
            for row in data:
                pri = ""
                for elem in row:
                    if delimiter in elem:
                        pri += delimiter+'"'+elem+'"'
                    else:
                        pri += delimiter+elem
                file.write(pri.replace(delimiter, "", 1)+"\n")
