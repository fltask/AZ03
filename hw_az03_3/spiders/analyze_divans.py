import matplotlib.pyplot as plt
import pandas as pd

# Чтение CSV с разделителем ';'
df = pd.read_csv('../results/divans.csv', delimiter=';')

# Очистка цен: удаляем все, кроме цифр и точек
df['price_clean'] = (
    df['price']
    .astype(str)
    .str.replace(r'[^\d.]', '', regex=True)
    .astype(float)
)

# Вычисление средней цены
avg_price = df['price_clean'].mean()

print(f"Средняя цена диванов: {avg_price:.2f}")

# Построение гистограммы цен
plt.figure()
plt.hist(df['price_clean'], bins=30)
plt.title("Гистограмма распределения цен на диваны")
plt.xlabel("Цена")
plt.ylabel("Количество")
plt.tight_layout()
plt.grid(True)
plt.show()
