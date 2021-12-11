import os.path

def read_csv (path_to_csv_file, delimiter = ","):
    data = [] 
    if os.path.isfile(path_to_csv_file):
        lines = open(path_to_csv_file, 'r', encoding='utf-8').readlines() 
        for l in lines:
            d = l.strip().split(delimiter, 1)
            data.append(d) 
    else:
        print('Error, such file doesn\'t exist')
    return data

def write_csv (path_to_csv_file, data, delimiter = ','):
    if data != None and data != []:
        f = open(path_to_csv_file, 'w', encoding='utf-8')
        for d in data:
            s = delimiter.join(d)  
            f.write(s + '\n')
    else:
        print('No data to write!')