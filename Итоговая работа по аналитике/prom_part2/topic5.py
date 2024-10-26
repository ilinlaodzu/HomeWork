# from scipy import stats

# mean_A = 360
# st_A = 40
# k_A = 9802

# mean_B = 352
# st_B = 58
# k_B = 9789

# # Выполним  тест Уэлча
# t_stat, p_value = stats.ttest_ind_from_stats(
#     mean1=mean_A, st1=st_A, nobs1=k_A,
#     mean2=mean_B, st2=st_B, nobs2=k_B,
#     equal_var=False  
# )

# # Выводим t-статистику и p-значение
# print(f'T-статистика: {t_stat:.2f} P-значение: {p_value}')


from scipy.stats import t

# Данные по группам
mean_a, std_a, n_a = 360, 40, 9802
mean_b, std_b, n_b = 352, 58, 9789

# Расчет t-статистики
t_stat = (mean_a - mean_b) / ((std_a**2 / n_a + std_b**2 / n_b) ** 0.5)

# Степени свободы по формуле Уэлча
df = ((std_a**2 / n_a + std_b**2 / n_b)**2) / ((std_a**2 / n_a)**2 / (n_a - 1) + (std_b**2 / n_b)**2 / (n_b - 1))

# p-value для двустороннего теста
p_value = 2 * (1 - t.cdf(abs(t_stat), df))

# Критическое значение t для alpha = 0.2
critical_t = t.ppf(1 - 0.2 / 2, df)

print(f"t-статистика: {t_stat:.2f}")
print(f"Критическое значение t: {critical_t:.2f}")
print(f"p-значение: {p_value:.5f}")

# Вывод результатов
if abs(t_stat) > critical_t:
    print("Результат статистически значим. Версия A показала лучшие результаты.")
else:
    print("Результат НЕ статистически значим. Версию B можно оставить на продакшн.")
