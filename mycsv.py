def read_csv(path_to_csv_file, delimeter):
    try:
        f = open(path_to_csv_file, "r")
    except OSError:
        print("Error, such file doesn't exist")
        exit(84)
    tab = []
    str = ""
    str2 = ""
    for item in f:
        if item[-1] == '\n':
            item = item[:-1]
        tab.append(item.split(delimeter))
        if len(tab[-1]) > 2 and tab[-1][1][0] == "\"":
            str = tab[1][1].replace("\"", "")
            str2 = tab[1][2].replace("\"", "")
            tab[1][1] = str + ',' + str2
            tab[1].pop()
            print(tab[1][1])
        elif len(tab[-1]) == 2 and tab[-1][1][0] == "\"":
            str = tab[-1][1].replace("\"", "")
            tab[-1][1] = str
    return tab