# Импорт всех необходимых библиотек
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Загрузка и исследование датасета Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

# Визуализация зависимостей
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
for species in iris.target_names:
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'],
                label=species, alpha=0.7)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title('Sepal Length vs Sepal Width')
plt.legend()

plt.subplot(1, 2, 2)
for species in iris.target_names:
    subset = df[df['species'] == species]
    plt.scatter(subset['petal length (cm)'], subset['petal width (cm)'],
                label=species, alpha=0.7)
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.title('Petal Length vs Petal Width')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Pairplot для всего датасета
sns.pairplot(df, hue='species', vars=iris.feature_names)
plt.show()

# 3. Подготовка датасетов для бинарной классификации
df_setosa_versicolor = df[df['target'].isin([0, 1])].copy()
df_versicolor_virginica = df[df['target'].isin([1, 2])].copy()
df_versicolor_virginica['target'] = df_versicolor_virginica['target'] - 1


# 4-8. Функция для обучения и оценки модели
def train_and_evaluate(df, features, target='target', test_size=0.3, random_state=42):
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)

    clf = LogisticRegression(random_state=0)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    train_accuracy = clf.score(X_train, y_train)

    print(f"Точность на обучающей выборке: {train_accuracy:.4f}")
    print(f"Точность на тестовой выборке: {accuracy:.4f}")

    return clf


# Применение к обоим датасетам
features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print("Классификация setosa vs versicolor:")
model1 = train_and_evaluate(df_setosa_versicolor, features)

print("\nКлассификация versicolor vs virginica:")
model2 = train_and_evaluate(df_versicolor_virginica, features)

# 9. Генерация синтетического датасета и классификация
X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0,
                           n_informative=2, random_state=1, n_clusters_per_class=1)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Сгенерированный датасет для бинарной классификации')
plt.colorbar()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = LogisticRegression(random_state=0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
train_accuracy = clf.score(X_train, y_train)

print("\nКлассификация на синтетическом датасете:")
print(f"Точность на обучающей выборке: {train_accuracy:.4f}")
print(f"Точность на тестовой выборке: {accuracy:.4f}")


# Визуализация разделяющей границы
def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Разделяющая граница логистической регрессии')
    plt.show()


plot_decision_boundary(X, y, clf)