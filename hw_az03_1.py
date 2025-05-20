import matplotlib.pyplot as plt
import numpy as np

# Гистограмма для случайных данных

# Параметры нормального распределения
mean = 0
std_dev = 1
num_samples = 1000

# Генерация данных
data = np.random.normal(loc=mean, scale=std_dev, size=num_samples)

# Построение гистограммы
plt.figure()  # отдельное пространство для рисования
plt.hist(data, bins=30)
plt.title("Гистограмма случайных данных из N(0,1)")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.tight_layout()  # автоматически подбирает оптимальные отступы между элементами графика (заголовком, осями, метками, легендой и т. д.)
plt.grid(True)
plt.show()

