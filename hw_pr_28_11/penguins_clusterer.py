import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


penguins = sns.load_dataset('penguins')

print('Датасет "Penguins" загружен.')

full_size = len(penguins)
print(f'Всего {full_size} записей.')

# Очищаем от данных с пропущенными значениями
penguins = penguins.dropna()

len_difference = full_size - len(penguins)
print(f'Удалено {len_difference} строк.')

# Выбор признаков для кластеризации: длина и глубина клюва, длина ласт, вес
features = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

scaler = StandardScaler()

# Стандартизируем выбранные признаки
scaled_features = scaler.fit_transform(features)
print('Стандартизировали.')

# Применение K-means с 3 кластерами
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)
print('K-Means применили.')

# Добавление результатов кластеризации в исходный DataFrame
penguins['cluster'] = clusters

print('-' * 30)

# Вывод количества элементов в каждом кластере
print("Размеры кластеров (сколько элементов принадлежит каждому кластеру):")
print(penguins['cluster'].value_counts())
print('-' * 30)


# Подсчет количества каждого вида, пола и острова
species_counts = penguins['species'].value_counts()
sex_counts = penguins['sex'].value_counts()
island_counts = penguins['island'].value_counts()

print('Группировка по кластерам')
print('-' * 30)

# Группировка по видам и кластерам
print("Группировка по видам и кластерам:")
print(penguins.groupby(['species', 'cluster']).size())
print('Показывает, как распределяются виды пингвинов по кластерам.')

print("Количество каждого вида пингвинов в исходных данных:")
for species, count in species_counts.items():
    print(f"{species}: {count}")
print('-' * 30)

# Группировка по полу и кластерам
print("Группировка по полу и кластерам:")
print(penguins.groupby(['sex', 'cluster']).size())
print('Позволяет увидеть распределение пингвинов по полу в каждом кластере.')

print("Количество пингвинов каждого пола в исходных данных:")
for sex, count in sex_counts.items():
    print(f"{sex}: {count}")
print('-' * 30)

# Группировка по острову и кластерам
print("Группировка по острову и кластерам:")
print(penguins.groupby(['island', 'cluster']).size())
print('Показывает распределение пингвинов по островам в каждом кластере.')

print("Количество пингвинов на каждом острове в исходных данных:")
for island, count in island_counts.items():
    print(f"{island}: {count}")
print('-' * 30)


print('Коэффициенты:')

# Вывод инерции (внутрикластерная дисперсия)
inertia = kmeans.inertia_
print(f"Inertia (внутрикластерная дисперсия): {inertia}")
print('Инерция показывает, насколько компактны кластеры. Меньшее значение указывает на более плотные кластеры.')

# Вычисление коэффициента силуэта
silhouette = silhouette_score(scaled_features, clusters)
print(f"Silhouette Score (коэффициент силуэта): {silhouette}")
print('Коэффициент силуэта измеряет, насколько хорошо точки кластеризованы. Значение близкое к 1 указывает на хорошую кластеризацию.')

print('-' * 30)


