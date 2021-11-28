import mycsv

# Testing basic data file 
lines1 = mycsv.read_csv("testdata.csv")

# Testing the case where the delimiter is included in content as well 
lines2 = mycsv.read_csv("testdata2.csv")

# Testing the case with another delimiter 
lines3 = mycsv.read_csv("testdata3.csv", delimiter = "*")


print("##### FIRST CASE #####\n")
print(lines1)
print("\n")
print("##### SECOND CASE #####\n")
print(lines2)
print("\n")
print("##### THIRD CASE #####\n")
print(lines3)
print("\n")


# Testing writing to a file

import mycsv
lines = [
['ID', 'Vlaue'],
['101', '10,5'],
['102', '11'],
['103','11.5']
]
mycsv.write_csv("data_1_writing.csv", lines)
mycsv.write_csv("data_2_writing.tsv", lines, delimiter="\t")

# Testing incorrect calls with writing: 

lines2 = "write these lines"
mycsv.write_csv("data_3_writing.csv", lines2)

lines3 = ["write these lines"]
mycsv.write_csv("data_4_writing.csv", lines3)


