#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
#о фирме: название, форма собственности, выручка, издержки.
#пример строки файла: firm1 ООО 10000 5000
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#Если фирма получила убытки, в расчет средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#Пример списка [{'firm_1':5000,'firm_2':3000,'firm_3':1000},{'average_profit':2000}]
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:[{'firm_1':5000,'firm_2':3000,'firm_3':1000},{'average_profit':2000}]
#Подсказка: использовать менеджер котекста

import json
from my_functions import check_not_string
final_list = []
profit = 0
i=0
summ_profit = 0
average_profit = 0
with open('hw7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        index_proceeds = ''
        split_line = line.replace("\n","").split(' ')
        for el in split_line:
            if check_not_string(el)==True:
                index_proceeds = split_line.index(el)
                profit = float(split_line[index_proceeds])-float(split_line[index_proceeds+1])
                if profit >= 0:
                    i+=1
                    summ_profit = summ_profit + profit
                    average_profit = summ_profit/i
                break
        dict = {" ".join(split_line[0:index_proceeds - 1]): profit}
        final_list.append(dict)
    final_list.append({'average_profit':average_profit})
with open('itog_json.json', 'w') as f:
    json.dump(final_list,f)
with open('itog_json.json', 'r') as f:
    data = json.load(f)
print(data)

