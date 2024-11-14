import pandas as pd

# Константы
DIVIDER = '-' * 30 + '\n'
TITLE = 'ОТЧЕТ\n' + DIVIDER

CSV_FILENAME = r'c:\dev\itmo\itmopython\hw_pr_07_10\data\recipes_full\recipes_full_0.csv'
df = pd.read_csv(CSV_FILENAME)

# Формируем отчет
report = TITLE

max_steps = df['n_steps'].max()
report += f'Максимальное значение столбца n_steps: {max_steps}\n'

graphomaniac = df['contributor_id'].mode()[0]
report += f'id пользователя, отправлявшего рецепты чаще всех: {graphomaniac}\n'

report += DIVIDER

# Берем самую раннюю и самую позднюю дату
earliest_date = df['submitted'].min()
latest_date = df['submitted'].max()

# Выбираем рецепты, опубликованные в самую раннюю и в самую позднюю даты
first_recipe = df[df['submitted'] == earliest_date]
last_recipe = df[df['submitted'] == latest_date]

report += f'Первая дата: {earliest_date}, рецептов: {first_recipe.shape[0]}\n' + DIVIDER
report += first_recipe.to_string() + '\n' + DIVIDER
report += f'Последняя дата: {latest_date}, рецептов: {last_recipe.shape[0]}\n' + DIVIDER
report += last_recipe.to_string() + '\n' + DIVIDER

ingredients_median = df['n_ingredients'].median()
minutes_median = df['minutes'].median()
report += f'Медианное значение количества ингридиентов: {ingredients_median}; медианное значение количества минут: {minutes_median}\n'
report += DIVIDER

# Фильтруем по минимальному кол-ву ингредиентов
min_ingredients = df['n_ingredients'].min()
filtered_by_ingredients = df[df['n_ingredients'] == min_ingredients]
if len(filtered_by_ingredients) > 1:
    # Фильтруем по минимальному затраченному времени
    # В некоторых рецептах мин. значение минут равно нулю, поэтому нам нужно следующее уникальное минимальное значение
    # Для этого удаляем дубликаты и берем второе мин. значение
    second_min_minutes = filtered_by_ingredients['minutes'].drop_duplicates().nsmallest(2).iloc[-1]
    filtered_by_minutes = filtered_by_ingredients[filtered_by_ingredients['minutes'] == second_min_minutes]
    if len(filtered_by_minutes) > 1:
        # Фильтруем по количеству шагов в рецепте
        min_steps = filtered_by_minutes['n_steps'].min()
        filtered_by_steps = filtered_by_minutes[filtered_by_minutes['n_steps'] == min_steps]
        if len(filtered_by_steps) > 0:
            decision = input(f'По минимальному кол-ву ингредиентов, минут и шагов отфильтровано {len(filtered_by_steps)} рецептов. Печатать? (y - да):')
            if decision == 'y':
                report += 'Рецепты с минимальным количеством ингредиентов\n' + DIVIDER
                report += filtered_by_steps.to_string()

print(report)

input('Нажмите Enter для завершения программы...')

