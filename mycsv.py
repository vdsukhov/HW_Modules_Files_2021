def read_csv(path, delimiter = ","):

  try:
    with open(path) as inp_f:

      lines = []
      
      for line in inp_f:
        line = line.strip()
        sep1 = '\'' if line.count('\'') > 0 else '\"'
        tmp = []

        while True:
          a = line.find(delimiter)
          b = line.find(sep1)
          if a == -1 and b == -1:
            if line != '':
              tmp.append(line)
            break
          elif b == -1 or (a < b and a != -1):
            tmp.append(line[:line.find(delimiter)])
            line = line[line.find(delimiter) + 1::]
          else:
            end = line[b+1::].find(sep1)
            tmp.append(line[b+1:end+1:])
            line = line[end+3::]
        
        lines.append(tmp)
      return lines

  except FileNotFoundError:
    print ("Error, such file doesn't exist")
    return []

def write_csv(path, lines, delimiter = ','):
  try:
    with open(path, 'w') as out_f:
      for i in range(len(lines)):
        tmp = []
        for j in range(len(lines[i])):
          if delimiter == ',' and lines[i][j].isnumeric() == False and lines[i][j].isalpha() == False:
            tmp.append('\"' + lines[i][j] + '\"')
          else:
            tmp.append(lines[i][j])
        out_f.write(delimiter.join(i for i in tmp) + '\n')
  except Exception:
    print ("Sorry, couldn't handle request")