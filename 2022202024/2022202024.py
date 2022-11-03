import csv

flag = 0;
ls = []
newls = []
with open('lab_11_data.csv' , mode ='r') as file :
  csvFile = csv.reader(file)
  
  for l in csvFile:
    
    ls.append(l[:-6])
    
for l in filter(lambda x: float(x[-1]) <= -3, ls[1:]):
  ls.remove(l)


op = list(map(lambda x: float(x[1].replace(',',''))  , ls[1:]))
op = sum(op)/len(op)
hp = list(map(lambda x: float(x[2].replace(',',''))  , ls[1:]))
hp = sum(hp)/len(hp)
lp = list(map(lambda x: float(x[3].replace(',',''))  , ls[1:]))
lp = sum(lp)/len(lp)

avg = [[op],[hp],[lp]]

with open('avg_output.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(avg)



indi = input("Enter character: ")
ans = []
for i in ls[1:]:
  if i[0][0] == indi:
    ans.append(i)
with open('stock_output.txt', 'w', newline='') as file:
    writer = csv.writer(file,delimiter=' ')
    writer.writerows(ans)
