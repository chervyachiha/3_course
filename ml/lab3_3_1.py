import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                           f1_score, confusion_matrix, precision_recall_curve,
                           roc_curve, auc, RocCurveDisplay, PrecisionRecallDisplay)

# Загрузка и предобработка данных
titanic = pd.read_csv(r'D:\уник\мл\LabML_3\Titanic.csv')
titanic_clean = titanic.dropna().copy()
cols_to_drop = ['Name', 'Ticket', 'Cabin', 'PassengerId']
titanic_clean = titanic_clean.drop(cols_to_drop, axis=1)

# Кодирование категориальных признаков
titanic_clean['Sex'] = LabelEncoder().fit_transform(titanic_clean['Sex'])
titanic_clean['Embarked'] = LabelEncoder().fit_transform(titanic_clean['Embarked']) + 1

# Разделение данных
X = titanic_clean.drop('Survived', axis=1)
y = titanic_clean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучение модели
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
y_pred = lr_model.predict(X_test)
y_proba = lr_model.predict_proba(X_test)[:, 1]

# 1. Вычисление метрик
print("Метрики для логистической регрессии:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1-score: {f1_score(y_test, y_pred):.4f}")

# 2. Матрица ошибок
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Не выжил', 'Выжил'],
            yticklabels=['Не выжил', 'Выжил'])
plt.title('Матрица ошибок')
plt.ylabel('Истинный класс')
plt.xlabel('Предсказанный класс')
plt.show()

# 3. Кривая PR
precision, recall, _ = precision_recall_curve(y_test, y_proba)
disp = PrecisionRecallDisplay(precision=precision, recall=recall)
disp.plot()
plt.title('Кривая Precision-Recall')
plt.show()

# 4. Кривая ROC
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
disp = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc)
disp.plot()
plt.title('ROC кривая')
plt.show()