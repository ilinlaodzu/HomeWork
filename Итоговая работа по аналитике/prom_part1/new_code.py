

import locale
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Устанавливаем русскую локаль для корректной обработки дат на русском
def set_russian_locale():
    try:
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # Для Linux/macOS
    except locale.Error:
        print("Не удалось установить русскую локаль.")


file_path = r"data2343last2.csv"
data = pd.read_csv(file_path, sep=';')  
# print(data)
# # Чтение и очистка данных
data.columns = data.columns.str.strip()  #  ишние пробелы в названиях колонок
cleaned_data_gc = data.dropna(
    subset=['Device Category', 'Region', 'Goal Completions']).copy()  # Удаление строк 
cleaned_data_date = data 

cleaned_data_date['Date'] = pd.to_datetime(cleaned_data_date['Date'], format='%d.%m.%Y', errors='coerce')
cleaned_data_date = cleaned_data_date.dropna(subset=['Date', 'Goal Completions'])
# print(cleaned_data_date)


# 1/Анализ регионов по количеству заявок
def analyze_regions(data):
    # print(data)
    region_counts = data.groupby('Region')['Goal Completions'].sum().sort_values(ascending=False)
    print("Лидеры регионов с наибольшим количеством заявок:")
    print(region_counts)
    print(region_counts.head(3))
        
    plt.figure(figsize=(12, 6))
    region_counts.head(3).plot(kind='bar')
    plt.title('Лидеры регионов по количеству заявок')
    plt.xlabel('Регион')
    plt.ylabel('Количество заявок')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

# 2/Анализ отказов
def analyze_bounce_rate(data):
    print("Анализ отказов:")
    # Проверяем наличие колонки Bounce Rate
    if 'Bounce Rate' in data.columns:
        # Преобразуем данные в числовой тип, заменяя любые некорректные значения на 0
        bounceRate = data['Bounce Rate']
        bounceRateSum = pd.to_numeric(bounceRate.str.replace('%', '').str.replace(',', '.'), errors='coerce').sum()
        avg = bounceRateSum/bounceRate.size
        print(avg)
        data['Bounce Rate'] = pd.to_numeric(data['Bounce Rate'], errors='coerce').fillna(0)
        # Рассчитываем средний процент отказов
        average_bounce_rate = data['Bounce Rate'].mean()
        print(f"Средний процент отказов: {average_bounce_rate:.2f}%")
    else:
        print("Колонка 'Bounce Rate' отсутствует в данных.")

# 3/Анализ устройств
def analyze_devices(data):
    device_counts = data['Device Category'].value_counts()
    print("Количество заходов с разных устройств:")
    # print(device_counts)
    
    plt.figure(figsize=(12, 6))
    device_counts.plot(kind='bar')
    plt.title('Заходы по устройствам')
    plt.xlabel('Устройства')
    plt.ylabel('Количество')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 4/Анализ источников по конверсиям
def analyze_sources(data):
    source_conversion_sum = data.groupby('Source')['Goal Completions'].sum().sort_values(ascending=False)
    print("Лидеры источников по количеству конверсий:")
    print(source_conversion_sum.head(5))
    
    plt.figure(figsize=(12, 6))
    source_conversion_sum.head(5).plot(kind='bar')
    plt.title('Лидеры источников по количеству конверсий')
    plt.xlabel('Источник')
    plt.ylabel('Количество конверсий')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 5/Анализ ROMI
average_car_price=5333674.179 
total_rev = cleaned_data_gc['Goal Completions'].sum() * average_car_price
def clean_numeric(value):
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        cleaned = ''.join(char for char in value if char.isdigit() or char in '.,')
        cleaned = cleaned.replace(',', '.')
        try:
            return float(cleaned)
        except ValueError:
            return np.nan
    return np.nan
numeric_columns = ['Sessions', 'Goal Completions']
for col in numeric_columns:
    cleaned_data_gc[col] = cleaned_data_gc[col].apply(clean_numeric)
grouped = cleaned_data_gc.groupby('Source').agg({
    'Sessions': 'sum',
    'Goal Completions': 'sum'
    })

grouped['Conversion Rate'] = grouped['Goal Completions'] / grouped['Sessions']
grouped['Revenue'] = grouped['Goal Completions'] * average_car_price
cost_per_session = 50
grouped['Marketing Cost'] = grouped['Sessions'] * cost_per_session
grouped['ROMI'] = (grouped['Revenue'] - grouped['Marketing Cost']) / grouped['Marketing Cost'] * 100
grouped_sorted = grouped.sort_values('ROMI', ascending=False)
print(f"Средняя стоимость проданного автомобиля: {average_car_price:.2f} руб.")
print("\nЛидеры источников по ROMI:")
print(grouped_sorted[['Sessions', 'Goal Completions', 'Revenue', 'Conversion Rate', 'Marketing Cost', 'ROMI']].head(10))

# 6/Посчитайте выручку в рублях только по долларовым позициям
usd_to_rub = 93  
# Курс доллара
cleaned_data_dol = data.dropna(
    subset=['Модель', 'Цена']).copy()
cleaned_data_dolsale=cleaned_data_dol[(cleaned_data_dol['Продажа']>0) & (cleaned_data_dol["Валюта"]=='Доллар США' )]
if cleaned_data_dolsale.size>0:
    dolsale_sum=pd.to_numeric(cleaned_data_dolsale['Цена'].str.replace(',', '.')).sum() * usd_to_rub
    print (f"Данные по долларовым позициям:   {dolsale_sum:.2f}   руб.")
else:
    print("Нет данных по позициям")

#  7/Прогноз до конца февраля по количеству конверсий на каждый день
if pd.api.types.is_datetime64_any_dtype(cleaned_data_date['Date']):
    # print(cleaned_data_date['Date'])
    daily_conversions = cleaned_data_date.groupby(cleaned_data_date['Date'].dt.date)['Goal Completions'].sum()
    max_febr_day = cleaned_data_date[((cleaned_data_date['Date'] > '02.01.2020') & (cleaned_data_date['Date'] < '29.02.2020'))]['Date'].max() + pd.DateOffset(1)
    # Проверяем, есть ли данные для прогноза
    if len(daily_conversions) > 0:
        forecast_days = pd.date_range(start=max_febr_day, end='29.02.2020')  # Прогноз на февраль
        print(forecast_days)
        average_daily_conversions = daily_conversions.mean()
        forecast_conversions = pd.Series(average_daily_conversions, index=forecast_days)
        print("Прогноз по количеству конверсий на февраль:")
        print(forecast_conversions)
    else:
        print("Нет данных для февраля.")
else:
        print("Колонка 'Date' не содержит данные типа datetime.")


# Средняя стоимость автомобиля
average_car_price = 5333674.179  # Задайте актуальное значение или используйте ваше
# 8/Прогноз выручки за первый квартал
# Прежде чем рассчитать выручку, необходимо вычислить общее количество конверсий
# Убедимся, что данные по конверсиям корректны
if 'Goal Completions' in cleaned_data_gc.columns and pd.api.types.is_datetime64_any_dtype(cleaned_data_date['Date']):
    # Группируем данные по дате, чтобы получить конверсии по каждому дню
    daily_conversions = cleaned_data_gc.groupby(cleaned_data_date['Date'].dt.date)['Goal Completions'].sum()
    # print (daily_conversions )
    # Если данные по ежедневным конверсиям есть
    if len(daily_conversions) > 0:
        # Общая выручка по текущим данным
        total_revenue = cleaned_data_gc['Goal Completions'].sum() * average_car_price
        # Прогноз на первый квартал (92 дня)
        q1_forecast_revenue = (total_revenue / len(daily_conversions.index)) * 92  
        # Пропорциональный прогноз
        print(f"Прогнозируемая выручка за первый квартал: {q1_forecast_revenue:.2f} руб.")
    else:
        print("Нет данных для прогнозирования конверсий.")
else:
    print("Колонка 'Goal Completions' или 'Date' содержит некорректные данные.")

# 9/Вспомогательная функция для преобразования числовых значений
def clean_numeric(value):
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        cleaned = ''.join(char for char in value if char.isdigit() or char in '.,')
        cleaned = cleaned.replace(',', '.')
        try:
            return float(cleaned)
        except ValueError:
            return np.nan
    return np.nan

# Вывод
def main():
    set_russian_locale()
    data_path = "data2343last2.csv"
    # cleaned_data = load_and_clean_data(data_path)
    # print(cleaned_data)
    
    # Лидеры региона
    analyze_regions(cleaned_data_gc)
    
    # Средний процент отказов
    analyze_bounce_rate(data)
    
    # Анализ устройств
    analyze_devices(data)
    
    # Источники по конверсиям
    analyze_sources(cleaned_data_gc)
    
    # Расчет ROMI
    average_car_price = 5333674.179 
    total_rev(cleaned_data_gc)

if __name__ == "__main__":
    main()