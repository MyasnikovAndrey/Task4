import pandas as pd

fr = pd.read_csv('fr3.csv', sep=';')

# ln = 2
# for i in range(ln):
for i in range(len(fr)):
    name = fr.values[i][1]
    descript = fr.values[i][2]
    rate = f'{fr.values[i][3]}'
    school = fr.values[i][4]
    start = fr.values[i][5]
    length = fr.values[i][6]
    price = fr.values[i][7]
    link = f'{fr.values[i][8]}'
    Tag = fr.values[i][9]
    print(name + ' ; ' + descript + ' ; ' + rate + ' ; ' + school + ' ; ' + start + ' ; ' + length + ' ; ' + price + ' ; ' + link + ' ; ' + Tag)