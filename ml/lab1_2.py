import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Вычисление коэффициентов a и b
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    a = numerator / denominator
    b = y_mean - a * x_mean

    return a, b


def main():
    # загрузить набор данных diabetes
    diabetes = datasets.load_diabetes()
    data = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    target = pd.Series(diabetes.target, name='target')

    # исследовать данные
    print("Описание набора данных:")
    print(diabetes.DESCR)
    print("\nПервые 5 строк данных:")
    print(data.head())

    # выбрать подходящий столбец для линейной регресии (возьмем 'bmi')
    feature_name = 'bmi'
    X = data[feature_name].values.reshape(-1, 1)
    y = target.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Реализовать метод линейной регрессии используя Scikit-Learn
    print("\nЛинейная регрессия с использованием Scikit-Learn:")
    model = LinearRegression()
    model.fit(X_train, y_train)

    a_sklearn = model.coef_[0]
    b_sklearn = model.intercept_
    print(f"Коэффициенты: a = {a_sklearn:.4f}, b = {b_sklearn:.4f}")

    # Реализовать метод линейной регрессии используя собственный алгоритм
    print("\nСобственная реализация линейной регрессии:")
    a_custom, b_custom = linear_regression(X_train.flatten(), y_train)
    print(f"Коэффициенты: a = {a_custom:.4f}, b = {b_custom:.4f}")

    # Сравнение коэффициентов
    print("\nСравнение коэффициентов:")
    print(f"Scikit-Learn: a = {a_sklearn:.4f}, b = {b_sklearn:.4f}")
    print(f"Собственный:  a = {a_custom:.4f}, b = {b_custom:.4f}")

    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, color='blue', alpha=0.5, label='Исходные данные')

    # Регрессионная прямая Scikit-Learn
    x_values = np.array([X.min(), X.max()])
    y_values_sklearn = a_sklearn * x_values + b_sklearn
    plt.plot(x_values, y_values_sklearn, color='red', linewidth=2,
             label=f'Scikit-Learn: y = {a_sklearn:.2f}x + {b_sklearn:.2f}')

    # Регрессионная прямая собственной реализации
    y_values_custom = a_custom * x_values + b_custom
    plt.plot(x_values, y_values_custom, color='green', linestyle='--', linewidth=2,
             label=f'Собственная:  y = {a_custom:.2f}x + {b_custom:.2f}')

    plt.xlabel(feature_name)
    plt.ylabel('Target (уровень заболевания)')
    plt.title('Линейная регрессия для набора данных diabetes')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Предсказания и таблица результатов
    print("\nТаблица результатов предсказаний:")
    y_pred_sklearn = model.predict(X_test)
    y_pred_custom = a_custom * X_test.flatten() + b_custom

    results = pd.DataFrame({
        'X_test': X_test.flatten(),
        'y_test': y_test,
        'Scikit-Learn pred': y_pred_sklearn,
        'Custom pred': y_pred_custom,
        'Scikit-Learn error': y_test - y_pred_sklearn,
        'Custom error': y_test - y_pred_custom
    })

    pd.set_option('display.max_columns', 6)
    print(results.head(10))

    print("\nОценка качества Scikit-Learn модели:")
    print(f"MAE: {mean_absolute_error(y_test, y_pred_sklearn):.2f}")
    print(f"R²: {r2_score(y_test, y_pred_sklearn):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred_sklearn):.2f}%")

    print("\nОценка качества собственной реализации:")
    print(f"MAE: {mean_absolute_error(y_test, y_pred_custom):.2f}")
    print(f"R²: {r2_score(y_test, y_pred_custom):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred_custom):.2f}%")

if __name__ == "__main__":
    main()