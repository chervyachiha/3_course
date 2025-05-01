# Импорт библиотек
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Загрузка данных с правильным путем (используйте raw строку или двойные слеши)
titanic = pd.read_csv(r'D:\уник\мл\LabML_3\Titanic.csv')

# 1. Предобработка данных
print("Исходный размер датасета:", titanic.shape)

# 1.1. Удаление строк с пропусками
titanic_clean = titanic.dropna()
print("Размер после удаления пропусков:", titanic_clean.shape)

# 1.2. Удаление нечисловых столбцов (оставляем только Sex и Embarked из категориальных)
cols_to_drop = ['Name', 'Ticket', 'Cabin', 'PassengerId']
titanic_clean = titanic_clean.drop(cols_to_drop, axis=1)

# 1.3. Перекодировка категориальных признаков
titanic_clean['Sex'] = LabelEncoder().fit_transform(titanic_clean['Sex'])
titanic_clean['Embarked'] = LabelEncoder().fit_transform(titanic_clean['Embarked']) + 1  # Чтобы получить 1,2,3

# 1.5. Процент потерянных данных
lost_percent = (len(titanic) - len(titanic_clean)) / len(titanic) * 100
print(f"Потеряно данных: {lost_percent:.2f}%")
print("\nОбработанный датасет:")
print(titanic_clean.head())

# 2. Машинное обучение
X = titanic_clean.drop('Survived', axis=1)
y = titanic_clean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2.2. Обучение модели
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# 2.3. Оценка точности
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nТочность модели: {accuracy:.4f}")

# 2.4. Оценка влияния Embarked
X_no_embarked = X.drop('Embarked', axis=1)
X_train_ne, X_test_ne, y_train_ne, y_test_ne = train_test_split(X_no_embarked, y, test_size=0.3, random_state=42)

model_ne = LogisticRegression(max_iter=1000, random_state=42)
model_ne.fit(X_train_ne, y_train_ne)

y_pred_ne = model_ne.predict(X_test_ne)
accuracy_ne = accuracy_score(y_test_ne, y_pred_ne)
print(f"Точность без признака Embarked: {accuracy_ne:.4f}")
print(f"Разница в точности: {accuracy - accuracy_ne:.4f}")

# Вывод коэффициентов модели
print("\nКоэффициенты модели:")
features = X.columns.tolist()
for feature, coef in zip(features, model.coef_[0]):
    print(f"{feature}: {coef:.4f}")