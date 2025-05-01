# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                           f1_score, confusion_matrix, precision_recall_curve,
                           roc_curve, auc, RocCurveDisplay, PrecisionRecallDisplay)
from IPython.display import Image

# Загрузка данных
diabetes = pd.read_csv('D:/уник/мл/LabML_5/diabetes.csv')
print(diabetes.head())
print("\nИнформация о датасете:")
print(diabetes.info())

# Разделение данных на признаки и целевую переменную
X = diabetes.drop('Outcome', axis=1)
y = diabetes['Outcome']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

## Задание 1: Сравнение логистической регрессии и решающего дерева

# Логистическая регрессия
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

print("\nМетрики логистической регрессии:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_lr):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_lr):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_lr):.4f}")
print(f"F1-score: {f1_score(y_test, y_pred_lr):.4f}")

# Решающее дерево (стандартные параметры)
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

print("\nМетрики решающего дерева (стандартные параметры):")
print(f"Accuracy: {accuracy_score(y_test, y_pred_tree):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_tree):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_tree):.4f}")
print(f"F1-score: {f1_score(y_test, y_pred_tree):.4f}")

## Задание 2: Исследование зависимости метрики от глубины дерева

# Выбираем F1-score как сбалансированную метрику между precision и recall
max_depths = range(1, 21)
f1_scores = []

for depth in max_depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    f1_scores.append(f1_score(y_test, y_pred))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(max_depths, f1_scores, marker='o')
plt.xlabel('Глубина дерева')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от глубины решающего дерева')
plt.grid(True)
plt.show()

# Определение оптимальной глубины
optimal_depth = max_depths[np.argmax(f1_scores)]
print(f"\nОптимальная глубина дерева: {optimal_depth}")

## Задание 3: Модель с оптимальной глубиной и визуализация (исправленная версия)

# Обучение модели с оптимальной глубиной
optimal_tree = DecisionTreeClassifier(max_depth=optimal_depth, random_state=42)
optimal_tree.fit(X_train, y_train)

try:
    # Попытка визуализации с помощью graphviz
    dot_data = export_graphviz(optimal_tree, out_file=None,
                               feature_names=X.columns,
                               class_names=['No Diabetes', 'Diabetes'],
                               filled=True, rounded=True,
                               special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render("diabetes_tree")  # Сохраняет в файл diabetes_tree.pdf
    print("Дерево сохранено в файл diabetes_tree.pdf")
except Exception as e:
    print(f"\nОшибка при визуализации дерева: {e}")
    print("Установите Graphviz для полной визуализации: https://graphviz.org/download/")

    # Альтернативная текстовая визуализация
    from sklearn.tree import export_text

    tree_rules = export_text(optimal_tree, feature_names=list(X.columns))
    print("\nТекстовое представление дерева решений:")
    print(tree_rules)

# Важность признаков
plt.figure(figsize=(10, 6))
feature_importances = pd.Series(optimal_tree.feature_importances_, index=X.columns)
feature_importances.sort_values().plot(kind='barh')
plt.title('Важность признаков в модели решающего дерева')
plt.show()

# PR и ROC кривые
y_proba = optimal_tree.predict_proba(X_test)[:, 1]

# PR кривая
precision, recall, _ = precision_recall_curve(y_test, y_proba)
disp = PrecisionRecallDisplay(precision=precision, recall=recall)
disp.plot()
plt.title('PR кривая для модели решающего дерева')
plt.show()

# ROC кривая
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
disp = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc)
disp.plot()
plt.title('ROC кривая для модели решающего дерева')
plt.show()