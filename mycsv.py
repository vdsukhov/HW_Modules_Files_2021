def read_csv(path_to_csv_file, delimiter=","):
    """
    This function takes two arguments: 1st is the path to
    the file, 2nd is the delimiter character. By default, the separator is a comma. The function should
    read the file and return a list of lines.
    """
    
    lines=[]
    try:
        with open(path_to_csv_file, "r") as f:
            line_f = f.readlines()
    except FileNotFoundError:
        print("Error, such file doesn't exist")
        return []
    
    for l in line_f:
        l = l.replace("\n", "")
        res_tmp=[]
        
        idx_quote1=l.find('\"')
        while idx_quote1 > -1:
            #do the first part of the string until the "
            res_tmp+=l[:idx_quote1].split(delimiter)[:-1]
            
            #add manually the word between the " "
            idx_quote2=l[idx_quote1+1:].find('\"')
            res_tmp.append(l[idx_quote1+1:idx_quote1+1+idx_quote2])
            
            #recompute the new l as the rest of the beginning list
            l=l[idx_quote1+3+idx_quote2:]
            idx_quote1 = l.find('\"')
        
        if len(l)==0:
            lines.append(res_tmp)
        else:
            lines.append(res_tmp + l.split(delimiter))
    
    return lines

def write_csv(path_to_csv_file, data, delimiter=','):
    """
    This function save data from data
    variable to the file with name path_to_csv_file using delimiter
    """
    
    if not(isinstance(path_to_csv_file, str) and isinstance(data, list) and isinstance(delimiter, str)):
        print("path_to_csv_file and delimiter should be a string and data should be a list")
        return
    
    with open(path_to_csv_file, "w") as f:
        for line in data:
            for i, element in enumerate(line):
                #find elements which contain delimiter
                if element.find(delimiter)>-1:
                    element='\"'+element+'\"'
                f.write(element)
                #add delimiter after all elements except the last
                if i<len(line)-1:
                    f.write(delimiter)
            f.write("\n")