import pandas
get_info = input() 
fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") 
info_list = fails.values.tolist() 
reg_name = 0

for x in range(len(info_list)):
    i = info_list[x][1]
    if i == get_info:
        reg_name = info_list[x][0]
        break
    
region = []
with open("data.csv","r") as f:
    next(f)
    for line in f:
        row = line.rstrip().split(",")
        if row[1] == reg_name:
            region.append(int(row[3])) 
print(sum(region))  