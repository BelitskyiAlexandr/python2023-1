import re


text_with_time_and_date = "Час: 12:34:56, Дата: 2023-11-03"

# Регулярні вирази для отримання списків часу, дати, годин та років
time_pattern = r'(\d{2}:\d{2}:\d{2})'
date_pattern = r'(\d{4}-\d{2}-\d{2})'
hour_pattern = r'\b(\d{1,2}):[0-5]\d:[0-5]\d\b' 
year_pattern = r'(\d{4})'

# Знаходження відповідних значень за допомогою регулярних виразів
times = re.findall(time_pattern, text_with_time_and_date)
dates = re.findall(date_pattern, text_with_time_and_date)
hours = re.findall(hour_pattern, text_with_time_and_date)
years = re.findall(year_pattern, text_with_time_and_date)

print(f"List of time: {times}")
print(f"List of date: {dates}")
print(f"List of hours: {hours}")
print(f"List of years: {years}")
