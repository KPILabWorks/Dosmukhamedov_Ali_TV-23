import pandas as pd
import numpy as np
import dask.dataframe as dd

# === Параметри генерації ===
num_rows = 1_000_000
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Helen", "Ivan", "Jack",
         "Kate", "Liam", "Mia", "Noah", "Olivia"]

# === Генерація першого датасету (ID + Name) ===
df1 = pd.DataFrame({
    "id": np.arange(1, num_rows + 1),
    "name": np.random.choice(names, num_rows)
})

df1.to_csv("name_dataset.csv", index=False)
print("Файл name_dataset.csv згенеровано!")

# === Генерація другого датасету (ID + Value) ===
df2 = pd.DataFrame({
    "id": np.arange(1, num_rows + 1),
    "value": np.round(np.random.uniform(5, 125, num_rows), 2)
})

df2.to_csv("value_dataset.csv", index=False)
print("Файл value_dataset.csv згенеровано!")


df1_dask = dd.read_csv("name_dataset.csv")
df2_dask = dd.read_csv("value_dataset.csv")

# Об'єднання двох датасетів по колонці "id"
merged_df = df1_dask.merge(df2_dask, on="id", how="outer")

# Створити пари ім'я - середнє значення
mean_values = merged_df.groupby("name")["value"].mean().round(2).compute()


# Виведення результату
print("\nСереднє значення 'value' для кожного імені:")
print(mean_values)
