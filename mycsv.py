import numpy as np
def read_csv(path_to_csv_file, delimiter=","):
    try:
        with open(path_to_csv_file, 'r') as csv_file:
            res = []
            for line in csv_file:
                line = line.strip()
                line = line.split(delimiter) 
                for el in line:
                    if el.startswith('"'):                
                        line_1 = ",".join(line[line.index(el):line.index(el)+2])
                        line[line.index(el):line.index(el)+2] = [line_1]
                        line = [el[1:-1] if el.startswith('"') else el for el in line]
                res.append(line)
            print(res)
    except FileNotFoundError:
        print("Error, such file doesn't exist:", [])

def write_csv(path_to_csv_file, data, delimiter=","):
    try:
        with open(path_to_csv_file, 'w') as out_f:
            for lst in data:
                out_f.writelines((delimiter.join(lst)) + "\n")
    except Exception:
        print("Error, couldn't complete your command")
