# Задача 4. Рост взрослого населения города X имеет нормальное распределение. Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см. Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см. б). больше 190 см. в). от 166 см до 190 см. г). от 166 см до 182 см. д). от 158 см до 190 см. е). не выше 150 см или не ниже 190 см. ё). не выше 150 см или не ниже 198 см. ж). ниже 166 см.

import numpy as np

std = 8 # сигма
mean = 174
growth_1 = 182
growth_2 = 190
growth_8 = 166

a = growth_1 - mean # интервал 1ой сигмы
print(a)

p_1 = (1 - 0.68) / 2
p_1proc = p_1 * 100
print("а) Вероятность того, что случайным образом выбранный взрослый человек имеет рост больше", growth_1, "см:", p_1, "или в процентах:", p_1proc)

b = growth_2 - mean
print(b)      
p_2 = (1 - 0.954) / 2 # интервал 2х сигм
p_2proc = p_2 * 100
print("б) Вероятность того, что случайным образом выбранный взрослый человек имеет рост больше", growth_2, "см:", p_2, "или в процентах:", p_2proc)

p_3 = (0.9545 + 0.68269) / 2 # по формуле Лапласа, используя таблицу Лапласа
p_3proc = p_3 * 100
print("в) Вероятность того, что случайным образом выбранный взрослый человек имеет рост от 166 см до 190 см", p_3, "или в процентах:", p_3proc)


p_4 = 0.68  # так как отклонения лежат в 1 сигме
p_4proc = p_4 * 100
print("г) Вероятность того, что случайным образом выбранный взрослый человек имеет рост от 166 см до 182 см:", p_4, "или в процентах:", p_4proc)

p_5 = 0.945 # так как отклонения лежат в 2х сигмах
p_5proc = p_5 * 100
print("д) Вероятность того, что случайным образом выбранный взрослый человек имеет рост от 158 см до 190 см:", p_5, "или в процентах:", p_5proc)

p_6 = (1- 0.9972) / 2 + p_2 
p_6proc = p_6 * 100
print("е) Вероятность того, что случайным образом выбранный взрослый человек имеет рост не выше 150 см или не ниже 190 см:", p_6, "или в процентах:", p_6proc)

p_7 = 1 - 0.9972 # так как отклонения лежат в 3х сигмах
p_7proc = p_7 * 100
print("ё) Вероятность того, что случайным образом выбранный взрослый человек имеет рост не выше 150 см или не ниже 198 см:", p_7, "или в процентах:", p_7proc)

# (growth_8  - mean) = 166 - 174 = -8 => -8 / 8 = -1 - ищем по таблице норм.распределения
p_8 = 0.1587
p_8proc = p_8 * 100
print("ж) Вероятность того, что случайным образом выбранный взрослый человек имеет рост ниже 166 см:", p_8, "или в процентах:", p_8proc)
