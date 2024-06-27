import matplotlib.pyplot as plt
import numpy as np

# Данные для графиков
occupancy_levels = [0, 35, 50, 55, 100]
occupancy_discounts = [14, 14, 7, 0, 0]

stay_lengths = [0, 5, 6, 10, 11, 20]
stay_discounts = [0, 0, 5, 5, 7, 7]

guest_counts = [1, 3, 4, 10]
guest_discounts = [0, 0, 5, 5]

months = list(range(1, 13))
seasonal_discounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5]

max_discount = 17

# График скидок по загруженности
plt.figure(figsize=(10, 5))
plt.plot(occupancy_levels, occupancy_discounts, marker='o', label='Скидка по загруженности')
plt.axhline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
plt.xlabel('Загруженность (%)')
plt.ylabel('Скидка (%)')
plt.title('Скидки по загруженности')
plt.legend()
plt.grid(True)
plt.show()

# График скидок по длительности пребывания
plt.figure(figsize=(10, 5))
plt.plot(stay_lengths, stay_discounts, marker='o', label='Скидка по длительности пребывания')
plt.axhline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
plt.xlabel('Длительность пребывания (дни)')
plt.ylabel('Скидка (%)')
plt.title('Скидки по длительности пребывания')
plt.legend()
plt.grid(True)
plt.show()

# График скидок по количеству гостей
plt.figure(figsize=(10, 5))
plt.plot(guest_counts, guest_discounts, marker='o', label='Скидка по количеству гостей')
plt.axhline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
plt.xlabel('Количество гостей')
plt.ylabel('Скидка (%)')
plt.title('Скидки по количеству гостей')
plt.legend()
plt.grid(True)
plt.show()

# График сезонных скидок
plt.figure(figsize=(10, 5))
plt.plot(months, seasonal_discounts, marker='o', label='Сезонная скидка')
plt.axhline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
plt.xlabel('Месяц')
plt.ylabel('Скидка (%)')
plt.title('Сезонная скидка')
plt.xticks(months, ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'])
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Данные для графиков
load_conditions = ['< 35% загруженности', '< 50% загруженности']
load_discounts = [14, 7]

stay_conditions = ['Пребывание 6-10 дней', 'Пребывание > 10 дней']
stay_discounts = [5, 7]

guest_condition = ['Гостей > 3']
guest_discount = [5]

season_condition = ['Декабрь']
season_discount = [5]

# Максимальная скидка
max_discount = 17

# Создание графиков
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# График скидок по загруженности
axs[0, 0].barh(load_conditions, load_discounts, color='skyblue')
axs[0, 0].axvline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
axs[0, 0].set_title('Скидки по загруженности')
axs[0, 0].set_xlabel('Процент скидки')
axs[0, 0].legend()

# Подписи к столбцам
for i, v in enumerate(load_discounts):
    axs[0, 0].text(v + 0.5, i, f"{v}%", color='blue', va='center')

# График скидок по длительности пребывания
axs[0, 1].barh(stay_conditions, stay_discounts, color='lightgreen')
axs[0, 1].axvline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
axs[0, 1].set_title('Скидки по длительности пребывания')
axs[0, 1].set_xlabel('Процент скидки')
axs[0, 1].legend()

# Подписи к столбцам
for i, v in enumerate(stay_discounts):
    axs[0, 1].text(v + 0.5, i, f"{v}%", color='blue', va='center')

# График скидок по количеству гостей
axs[1, 0].barh(guest_condition, guest_discount, color='lightcoral')
axs[1, 0].axvline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
axs[1, 0].set_title('Скидки по количеству гостей')
axs[1, 0].set_xlabel('Процент скидки')
axs[1, 0].legend()

# Подписи к столбцам
axs[1, 0].text(guest_discount[0] + 0.5, 0, f"{guest_discount[0]}%", color='blue', va='center')

# График сезонных скидок
axs[1, 1].barh(season_condition, season_discount, color='orange')
axs[1, 1].axvline(max_discount, color='red', linestyle='--', label='Максимальная скидка (17%)')
axs[1, 1].set_title('Сезонная скидка')
axs[1, 1].set_xlabel('Процент скидки')
axs[1, 1].legend()

# Подписи к столбцам
axs[1, 1].text(season_discount[0] + 0.5, 0, f"{season_discount[0]}%", color='blue', va='center')

# Уплотнение макета
plt.tight_layout()
plt.show()
