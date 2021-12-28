# This is a  Python script for the Module 12.7.3.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This script will calculate the amount of income per year per bank and presenting maximum value

# Input data
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money_raw = input("\nВведите сумму, которую вы можете положить в банк и нажмите 'Enter': ")
# check the correct input
while money_raw.isdigit() is False:
    money_raw = input("Ошибка, должно быть целое число \n"
                      "Введите заново сумму, которую вы можете положить в банк и нажмите 'Enter': ")

money = int(money_raw)

# combining the list
per_cent_numbers = list(per_cent.values())
# calculating percent
deposit = list(map(lambda x: x * money / 100, per_cent_numbers))
deposit_financial = list(map(round, deposit))
# print('deposit = ' + str(deposit))
print('deposit = ' + str(deposit_financial))

# printing max value
print("\nМаксимальная сумма, которую вы можете заработать - " + str(round(max(deposit), 2)))

# alternate solution
per_cent_banks = list(per_cent.keys())
max_index = deposit.index(max(deposit))
print("\nМаксимальная сумма, которую вы можете заработать - " + str(deposit_financial[max_index])
      + ' в банке ', '\033[1m' + '\033[4m' + per_cent_banks[max_index] + '\033[0m')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
