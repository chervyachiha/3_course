# Импорт библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, precision_recall_curve,
                             roc_curve, auc, RocCurveDisplay, PrecisionRecallDisplay)
from sklearn.preprocessing import LabelEncoder

# Загрузка и предобработка данных
titanic = pd.read_csv(r'D:\уник\мл\LabML_3\Titanic.csv')
titanic_clean = titanic.dropna().copy()
cols_to_drop = ['Name', 'Ticket', 'Cabin', 'PassengerId']
titanic_clean = titanic_clean.drop(cols_to_drop, axis=1)

# Кодирование категориальных признаков
titanic_clean['Sex'] = LabelEncoder().fit_transform(titanic_clean['Sex'])
titanic_clean['Embarked'] = LabelEncoder().fit_transform(titanic_clean['Embarked']) + 1

# Разделение данных - ЭТО НУЖНО ДОБАВИТЬ ПЕРЕД ИСПОЛЬЗОВАНИЕМ
X = titanic_clean.drop('Survived', axis=1)
y = titanic_clean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Функция для оценки моделей
def evaluate_model(model, X_train, X_test, y_train, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(X_test)

    # Метрики
    print(f"\nМетрики для {model_name}:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1-score: {f1_score(y_test, y_pred):.4f}")

    # Матрица ошибок
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Не выжил', 'Выжил'],
                yticklabels=['Не выжил', 'Выжил'])
    plt.title(f'Матрица ошибок ({model_name})')
    plt.ylabel('Истинный класс')
    plt.xlabel('Предсказанный класс')
    plt.show()

    # Кривые PR и ROC
    precision, recall, _ = precision_recall_curve(y_test, y_proba)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    PrecisionRecallDisplay(precision=precision, recall=recall).plot(ax=ax1)
    ax1.set_title(f'PR кривая ({model_name})')

    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot(ax=ax2)
    ax2.set_title(f'ROC кривая ({model_name})')

    plt.tight_layout()
    plt.show()


# Модель опорных векторов
svm_model = SVC(probability=True, random_state=42)
evaluate_model(svm_model, X_train, X_test, y_train, y_test, "SVM")

# Модель ближайших соседей
knn_model = KNeighborsClassifier()
evaluate_model(knn_model, X_train, X_test, y_train, y_test, "KNN")
