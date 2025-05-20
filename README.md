# AZ03

### Задание
1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
   - Параметры нормального распределения:
     - mean = 0 # Среднее значение
     - std_dev = 1 # Стандартное отклонение
     - num_samples = 1000 # Количество образцов

   - Генерация случайных чисел, распределенных по нормальному распределению
     - `data = np.random.normal(mean, std_dev, num_samples)`

2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`
   ```python
   import numpy as np
   random_array = np.random.rand(5) # массив из 5 случайных чисел
   print(random_array)
   ```

3. Необходимо спарсить цены на диваны с сайта [divan.ru](https://divan.ru):
   - сохранить csv файл
   - найти среднюю цену и вывести ее
   - сделать гистограмму цен на диваны
   ```bash
   scrapy startproject hw_az03_3
   cd hw_az03_3
   scrapy genspider divan_spider divan.ru
   ```
