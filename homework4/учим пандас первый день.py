import csv
import pandas as pd
import numpy as np

#first

#пропуски
df = pd.read_csv('/tested (1).csv')
total_miss = df.isnull().sum().sum()
zero_columns = df.isnull().sum()

print("Количество пропусков: ", total_miss)
print("\nКолонки с пропущенными значениями:")
print(zero_columns)

#тип данных
print("\nТип данных по колонкам:")
print(df.dtypes)

#первые и последние n строк
print("Ввидите сколько строк с начала и с конца необходимо вывести:")
lines = int(input())
print(f"\nПервые {lines} строки:")
print(df.head(lines))
print(f"\nПоследние {lines} строки:")
print(df.tail(lines))

#статистика по цене
print("\nОснавная статистика по цене за билет:")
print(df['Fare'].describe())

#количество строк и столбцов
rows, cols = df.shape
print("\nКоличество строк данных:", rows)
print("Количество строк в таблице", rows + 1)
print("Количество столбцов:", cols)

#пропуски в 'Age'
Age_skip = df['Age'].isnull().sum()
print(f"\nКоличество пропусков в столбце 'Age': {Age_skip}")
median = df['Age'].median()
df['Age'] = df['Age'].fillna(median)
print(f"\nПропуски заполнены медианой возраста: {median}")

#удаление 20 строк с неизвестным признаком
print(f"\nИзначальное количество строк: {len(df)}")
miss = df[df.isnull().any(axis=1)]
drops = miss.head(20).index
df=df.drop(drops)
print(f"Количество строк после удаления: {len(df)}")

#second

#1) Сравнение мужчик и женщин
# a. процент выживших
print("\n1) a.")
survived_by_sex = (df.groupby('Sex')['Survived'].mean() * 100).reset_index()
print(survived_by_sex)

# b. средний возраст
print("\n1) b.")
average_age_by_sex = df.groupby('Sex')['Age'].mean().reset_index()
print(average_age_by_sex)

# c. средний возраст выживших и погибших
print("\n1) c.")
average_age_surv_by_sex= df.groupby(['Sex', 'Survived'])['Age'].mean().reset_index()
average_age_surv_by_sex['Survived'] = average_age_surv_by_sex['Survived'].map({0: 'Dead', 1: 'Survives'})
print(average_age_surv_by_sex)

#2) Фильтрация

# a. Старше 30, Мужчины, 1 класс
print("\n2) a.")
filter_man_und30_1cl = df[(df['Age'] > 30) & (df['Sex'] == 'male') & (df['Pclass'] == 1)]
print(f"Нашлось: {len(filter_man_und30_1cl)} человек удовлетворяющих условиям: Мужчина, Старше 30, Первый класс.")
print(filter_man_und30_1cl.head())

# b. Моложе 18 ИЛИ женщины, которые выжили
print("\n2) b.")
filter_und18_or_surv_wmn = df[((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)]
print(f"Нашлось: {len(filter_und18_or_surv_wmn)} человек удовлетворяющих условиям: Младше 18 лет, или Женщины, которые выжили.")
print(filter_und18_or_surv_wmn.head())

#3) Группировка по классу и полу

grouping = df.groupby(['Pclass', 'Sex'])

# a. Средний возраст
print("\n3) a.")
print(grouping['Age'].mean().reset_index())

# b. Доля выживших
print("\n3) b.")
print((grouping['Survived'].mean() * 100).reset_index())

# c. Средняя стоимость билета
print("\n3) c.")
print(grouping['Fare'].mean().reset_index())

