
import pandas as pd

file_path = 'ab_stats.csv'
ab_stats_df = pd.read_csv(file_path)
# Фильтрация по признаку num_purchases > 0
paying_users = ab_stats_df[ab_stats_df['num_purchases'] > 0]
print(paying_users)
# расчет пользователей, дохода, А/В
grouped_data = paying_users.groupby('ab_group').agg(
    total_revenue=('revenue', 'sum'),
    paying_users=('revenue', 'count')
)
#  ARPPU  для групп
grouped_data['ARPPU'] = grouped_data['total_revenue'] / grouped_data['paying_users']

print(grouped_data)

