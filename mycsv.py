def test():
    return "module is working"

def read_csv(path_to_csv_file, delimiter=","):
    stopper = 0
    while stopper < 1:
        try:
            file = open(path_to_csv_file)
            output = []
            first_line = file.readline()
            first_line = first_line.replace("\n", "").split(delimiter)
            output.append(first_line)
            ncol = len(first_line)
            for elem in file:
                elem_demitered = elem.replace("\n", "").split(delimiter)
                if len(elem_demitered) == ncol:
                    output.append(elem_demitered)
            if len(elem_demitered) > ncol:
                    elem_not_demitered = elem
                    address_of_qoutes = []
                    address_of_delimiters = []
                    list1 = list(elem_not_demitered.strip(''))
                    for k in range(len(list1)):
                        if list1[k] == delimiter:
                            address_of_delimiters.append(k)
                        elif list1[k] == '\"':
                            address_of_qoutes.append(k)
                    for j in range(0, len(address_of_qoutes), 2):
                        for i in range(len(address_of_delimiters)):
                            I = address_of_delimiters[i]
                            J = address_of_qoutes[j]
                            if  I > J and I < J + address_of_qoutes[j + 1]:

                                None
                            else:
                                list1[I] = list1[I].replace(delimiter, 'ß')


                    #print(address_of_qoutes)
                    #print(address_of_delimiters)

                    not_final_string = ''.join(e for e in list1)
                    final_string = not_final_string.replace("\"", "")
                    final_line = final_string.replace("\n", "").split('ß')
                    output.append(final_line)


            file.close
            for i in range(len(output)):
                print(output[i])
            stopper = 1
        except FileNotFoundError:
            print("Error, such file doesn't exist")
            stopper = 1
    return ('by Evgenii Raines')

def write_csv(path_to_csv_file, data, delimiter=','):
    stopper = 0
    while stopper < 1:
        try:
            with open(path_to_file, "r") as file_csv:
                for line in file_csv:
                    line = line.strip()
                    line = line.split(delimiter)
                        for i in range(len(line)):
                            leego = -1
                            counter = 0
                            while True:
                                leego = line[i].find('"', leego+1)
                                if leego == -1:
                                    break
                                counter += 1
                                if counter == 2:
                                    line[i]=re.sub('["]',"",line[i])
                                if counter == 1:
                                    if line[i].find('"') == 0:
                                        line[i] = line[i]+delimiter+line[i+1]
                                        line[i]=re.sub('["]',"",line[i])
                        final_list.append(line)
                        for list in final_list:
                            for elem in list:
                                if elem.find('"') != -1:
                                    list.remove(elem)   
                file_csv.close()
                # in fact there are too many lines but anyway
                print(final_list)
                return("by Evgenii Raines")
                stopper = 1

        except FileNotFoundError:
            print("Error, such file doesn't exist")
            stopper = 1
    return ('by Evgenii Raines')  
