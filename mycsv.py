def read_csv(path_to_csv_file, delimiter=','):
    # import re
    import regex as re
    out = []
    try:
        file = open(path_to_csv_file)
        textini = file.read()
        text = textini.replace(delimiter, '~')
        print(textini)
        print(text)
        lines = text.split('\n')
        for line in lines:
            print(line)
            # out.append(line.split(delimiter))
            rx = re.compile(r'"[^"]*"(*SKIP)(*FAIL)|~\s*')
            o = rx.split(line)
            oo = [x.replace('~', delimiter) for x in o]
            out.append(oo)
            # out.append(re.split(r',(?=")', line))
    except:
        print("Error, such file doesn't exist")
    return out


def write_csv(path_to_csv_file, lines, delimiter=','):
    f = open(path_to_csv_file, "w")
    for line in lines:
        for i in range(len(line) - 1):
            if delimiter in line[i]:
                print(delimiter)
                line[i] = '"' + line[i] + '"'
                print(line[i])
            f.write(line[i] + delimiter)
        if delimiter in line[i + 1]:
            print(delimiter)
            line[i + 1] = '"' + line[i + 1] + '"'
        f.write(line[i + 1])
        f.write("\n")
    f.close()
    return f