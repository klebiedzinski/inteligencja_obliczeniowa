import pandas
from matplotlib import pyplot as plocisko

# a)
miasta = pandas.read_csv("/home/ubuntu/learning/inteligencja_obliczeniowa/lab01/miasta.csv", sep=",")
print(miasta)
print(miasta.values)

# b)
row = {
    'Rok': [2010],
    'Gdansk': [460],
    'Poznan': [555],
    'Szczecin': [405]
}
df = pandas.DataFrame(row)

# df.to_csv('/home/ubuntu/learning/inteligencja_obliczeniowa/lab01/miasta.csv', mode='a', index=False, header=False, columns=['Rok', 'Gdansk', 'Poznan', 'Szczecin'])
# miasta = pandas.read_csv("/home/ubuntu/learning/inteligencja_obliczeniowa/lab01/miasta.csv", sep=",")
# print(miasta)

# c)

plocisko.plot(miasta['Rok'], miasta['Gdansk'], label='Gdansk')
plocisko.show()