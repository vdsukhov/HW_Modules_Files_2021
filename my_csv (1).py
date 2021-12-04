from os import path
def read_csv(path_to_csv_file, delimiter = ","):
    if path.exists(path_to_csv_file) == False:
        print("Error, such file doesn't exist")
        return []       
    with open(path_to_csv_file) as f:
        results = []
        for line in f:
            quotes = False
            for char in line:
                if char == '"':
                    quotes = True
                elif delimiter == ',' and quotes == True:
                    delimiter = ' ,'
                else:
                    delimiter = ','
            line = line.replace(delimiter, ",").replace('\"','').strip("\n")
            results.append(line.split(delimiter))
        return results

def write_csv(path_to_csv_file, data, delimiter = ','):
    with open(path_to_csv_file, "a") as f:
        for line in data:
            if path_to_csv_file.split('.').pop() == 'csv':
                f.write(f'%s{delimiter}%s\n' % tuple(line))
            else:
                f.write(f'%s{delimiter}%s\n' % tuple(line))
        
        


