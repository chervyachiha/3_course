# Импорт библиотек
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions

# Загрузка данных
iris = load_iris()
X = iris.data[:, [2, 3]]  # Берем только petal length и petal width
y = iris.target

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучение модели многоклассовой логистической регрессии
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Оценка точности
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy:.4f}")

# Визуализация решений на плоскости
plt.figure(figsize=(10, 6))
plot_decision_regions(X, y, clf=model, legend=2)
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.title('Многоклассовая логистическая регрессия на Iris dataset')
plt.show()

# Вывод коэффициентов модели
print("\nКоэффициенты модели:")
for i, class_name in enumerate(iris.target_names):
    print(f"{class_name}: {model.coef_[i]}")