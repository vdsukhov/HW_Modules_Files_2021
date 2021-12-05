import os.path
def read_csv(path_to_csv_file, delimiter= ","):
    if os.path.exists(path_to_csv_file) == True: 
        answer = []
        with open(path_to_csv_file) as inp:
            for line in inp:
                line = line.strip('\n')
                lin = line.split(delimiter)
                for i in range(len(lin)-1, 0, -1):
                    if lin[i].endswith('"'):
                        lin[i] = lin[i][:-1]
                        if lin[i].startswith('"'):
                            lin[i] = lin[i][1:]
                        else:
                            lin[i-1] = lin[i-1][1:]
                            lin[i-1] = ','.join(lin[(i-1):(i+1)])
                            lin.remove(lin[i])
                            break
                    
                answer.append(lin)            
        return answer
    else:
        print("Error, such file doesn't exist")
        return []


def write_csv(path_to_csv_file, data, delimiter=','):
    with open (path_to_csv_file, 'w') as out:
        for string in data:
            answ = ''
            for elem in string:
                if ',' in elem or '.' in elem:
                    if string.index(elem) == 0:
                        answ +='"'+elem+'"'
                    else:
                        answ +=delimiter+'"'+elem+'"'
                else:
                    if string.index(elem) == 0:
                        answ+=elem
                    else:
                        answ+=delimiter+elem
                    
            out.write(answ+'\n')
        

