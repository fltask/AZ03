import numpy as np
import matplotlib.pyplot as plt

# Диаграмма рассеяния для двух наборов случайных данных

# Генерация двух наборов случайных данных по 5 точек каждый
x = np.random.rand(5)
y = np.random.rand(5)

# Построение диаграммы рассеяния
plt.figure()  # отдельное пространство для рисования
plt.scatter(x, y)
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout() # автоматически подбирает оптимальные отступы между элементами графика
plt.grid(True)
plt.show()