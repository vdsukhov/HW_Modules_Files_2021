import re

def read_csv(path_to_file, delimiter=','):
  new_list = []
  try:
    with open(path_to_file, "r") as file_csv:
      for line in file_csv:
        line = line.strip()
        line = line.split(delimiter)
        for i in range(len(line)):
          start = -1
          count = 0
          while True:
            start = line[i].find('"', start+1)
            if start == -1:
              break
            count += 1
          if count == 2:
            line[i]=re.sub('["]',"",line[i])
          if count == 1:
            if line[i].find('"') == 0:
              line[i] = line[i]+delimiter+line[i+1]
              line[i]=re.sub('["]',"",line[i])
        new_list.append(line)
        for list in new_list:
          for elem in list:
            if elem.find('"') != -1:
              list.remove(elem)   
    file_csv.close()
    return(new_list)
  except FileNotFoundError:
    return("Error, such file doesn't exist")


import os.path
def write_csv(path_to_csv_file, data, delimiter=','):
  try:
    with open(path_to_csv_file, "w") as create_file:
      for elem in data:
        n = len(elem)
        if os.path.splitext(path_to_csv_file)[1] == '.csv':
          for i in range(n):
            if elem[i].find(",") != -1 or elem[i].find(".") != -1:
              create_file.write('"'+elem[i]+'"')
            else:
              create_file.write(elem[i])
              if i == n-1:
                continue
              else:
                create_file.write(delimiter)
          create_file.write("\n")
          
        if os.path.splitext(path_to_csv_file)[1] == '.tsv':
          for i in range(n):
            create_file.write(elem[i])
            if i == n-1:
              continue
            else:
              create_file.write(delimiter)
          create_file.write("\n")
    create_file.close()
  except RuntimeError:
    return("Incorrect call")



    
      


  


