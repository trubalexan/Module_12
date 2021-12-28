# This is a  Python script for the Module 12.7.3.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This script will calculate which amount of income per year per bank

# Input data
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money_raw = input("Введите сумму, которую вы можете положить в банк и нажмите 'Enter':")
# check the correct input
while money_raw.isdigit() == False:
    money_raw = input("Ошибка. Введите заново сумму, которую вы можете положить в банк и нажмите 'Enter':")

money = int(money_raw)


# combining the list
per_cent_numbers = list(per_cent.values())
# calculating percent
deposit = list(map(lambda x: x * money/100, per_cent_numbers))
# print(deposit)

# printing max value
print("Максимальная сумма, которую вы можете заработать - " + str(round(max(deposit), 2)))

# alternate solution
max_index = deposit.index(max(deposit))
print("Максимальная сумма, которую вы можете заработать - " + str(round(deposit[max_index], 2)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
