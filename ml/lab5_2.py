# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                           f1_score, confusion_matrix, roc_auc_score)
from xgboost import XGBClassifier
from sklearn.tree import plot_tree

# Загрузка данных
diabetes = pd.read_csv('D:/уник/мл/LabML_5/diabetes.csv')
X = diabetes.drop('Outcome', axis=1)
y = diabetes['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

## Задание 1: Случайный лес

### 1.1 Исследование зависимости от глубины деревьев
max_depths = range(1, 21)
f1_scores_depth = []
train_times_depth = []

for depth in max_depths:
    start_time = time.time()
    model = RandomForestClassifier(max_depth=depth, n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    train_times_depth.append(time.time() - start_time)
    y_pred = model.predict(X_test)
    f1_scores_depth.append(f1_score(y_test, y_pred))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(max_depths, f1_scores_depth, marker='o')
plt.xlabel('Максимальная глубина деревьев')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от глубины деревьев')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(max_depths, train_times_depth, marker='o', color='orange')
plt.xlabel('Максимальная глубина деревьев')
plt.ylabel('Время обучения (сек)')
plt.title('Зависимость времени обучения от глубины деревьев')
plt.grid(True)
plt.tight_layout()
plt.show()

### 1.2 Исследование зависимости от количества признаков
max_features_range = range(1, len(X.columns)+1)
f1_scores_features = []
train_times_features = []

for n_features in max_features_range:
    start_time = time.time()
    model = RandomForestClassifier(max_features=n_features, n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    train_times_features.append(time.time() - start_time)
    y_pred = model.predict(X_test)
    f1_scores_features.append(f1_score(y_test, y_pred))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(max_features_range, f1_scores_features, marker='o')
plt.xlabel('Количество признаков для разбиения')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от количества признаков')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(max_features_range, train_times_features, marker='o', color='orange')
plt.xlabel('Количество признаков для разбиения')
plt.ylabel('Время обучения (сек)')
plt.title('Зависимость времени обучения от количества признаков')
plt.grid(True)
plt.tight_layout()
plt.show()

### 1.3 Исследование зависимости от количества деревьев
n_estimators_range = [10, 50, 100, 150, 200, 250, 300]
f1_scores_estimators = []
train_times_estimators = []

for n_est in n_estimators_range:
    start_time = time.time()
    model = RandomForestClassifier(n_estimators=n_est, random_state=42)
    model.fit(X_train, y_train)
    train_times_estimators.append(time.time() - start_time)
    y_pred = model.predict(X_test)
    f1_scores_estimators.append(f1_score(y_test, y_pred))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(n_estimators_range, f1_scores_estimators, marker='o')
plt.xlabel('Количество деревьев')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от количества деревьев')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(n_estimators_range, train_times_estimators, marker='o', color='orange')
plt.xlabel('Количество деревьев')
plt.ylabel('Время обучения (сек)')
plt.title('Зависимость времени обучения от количества деревьев')
plt.grid(True)
plt.tight_layout()
plt.show()

## Задание 2: XGBoost

# Подбор гиперпараметров XGBoost
params = {
    'max_depth': 3,
    'learning_rate': 0.1,
    'n_estimators': 100,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'reg_alpha': 0.1,
    'reg_lambda': 1,
    'objective': 'binary:logistic',
    'random_state': 42
}

start_time = time.time()
xgb_model = XGBClassifier(**params)
xgb_model.fit(X_train, y_train)
xgb_train_time = time.time() - start_time

y_pred_xgb = xgb_model.predict(X_test)
y_proba_xgb = xgb_model.predict_proba(X_test)[:, 1]

print("\nМетрики XGBoost:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_xgb):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_xgb):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_xgb):.4f}")
print(f"F1-score: {f1_score(y_test, y_pred_xgb):.4f}")
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_xgb):.4f}")
print(f"Время обучения: {xgb_train_time:.4f} сек")

# Сравнение с лучшей моделью случайного леса
best_rf = RandomForestClassifier(n_estimators=150, max_depth=5, max_features=3, random_state=42)
best_rf.fit(X_train, y_train)
y_pred_rf = best_rf.predict(X_test)

print("\nМетрики лучшей модели случайного леса:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_rf):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_rf):.4f}")
print(f"F1-score: {f1_score(y_test, y_pred_rf):.4f}")
print(f"AUC-ROC: {roc_auc_score(y_test, best_rf.predict_proba(X_test)[:, 1]):.4f}")

# Визуализация важности признаков
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
pd.Series(best_rf.feature_importances_, index=X.columns).sort_values().plot(kind='barh')
plt.title('Важность признаков (Random Forest)')

plt.subplot(1, 2, 2)
pd.Series(xgb_model.feature_importances_, index=X.columns).sort_values().plot(kind='barh')
plt.title('Важность признаков (XGBoost)')
plt.tight_layout()
plt.show()