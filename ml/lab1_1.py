import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. Реализовать чтение данных из файла
def read_data(filename):
    data = pd.read_csv(filename)
    return data

#2.	Вывести статистическую информацию о используемых данных (количество, min, max, среднее) по каждому из столбцов
def print_statistics(data, x_col, y_col):
    print("\nСтатистика по столбцу X:")
    print(f"Количество: {len(data[x_col])}")
    print(f"Минимальное значение: {data[x_col].min()}")
    print(f"Максимальное значение: {data[x_col].max()}")
    print(f"Среднее значение: {data[x_col].mean()}")

    print("\nСтатистика по столбцу Y:")
    print(f"Количество: {len(data[y_col])}")
    print(f"Минимальное значение: {data[y_col].min()}")
    print(f"Максимальное значение: {data[y_col].max()}")
    print(f"Среднее значение: {data[y_col].mean()}")

#4.	Реализовать алгоритм метода наименьших квадратов и вычислить параметры регрессионной прямой.
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

# должны одновременно видны все 3 изображения
def plot_all_graphs(data, x_col, y_col, a, b):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    # 3.	Используя библиотеку Matplotlib вывести изображение исходных точек
    ax1.scatter(data[x_col], data[y_col], color='blue', label='Исходные данные')
    ax1.set_xlabel(x_col)
    ax1.set_ylabel(y_col)
    ax1.set_title('Исходные данные')
    ax1.legend()
    ax1.grid(True)

    #5.	Используя библиотеку Matplotlib и полученное в п.2 изображение отрисовать на изображении другим цветом полученную прямую
    ax2.scatter(data[x_col], data[y_col], color='blue', label='Исходные данные')
    x_values = np.array([data[x_col].min(), data[x_col].max()])
    y_values = a * x_values + b
    ax2.plot(x_values, y_values, color='red', label='Регрессионная прямая')
    ax2.set_xlabel(x_col)
    ax2.set_ylabel(y_col)
    ax2.set_title('Регрессионная прямая')
    ax2.legend()
    ax2.grid(True)

    #6.	Используя полученное в п.4 изображение, отрисовать и заштриховать квадраты ошибок
    ax3.scatter(data[x_col], data[y_col], color='blue', label='Исходные данные')
    ax3.plot(x_values, y_values, color='red', label='Регрессионная прямая')
    for xi, yi in zip(data[x_col], data[y_col]):
        y_pred = a * xi + b
        left = min(xi, xi)
        right = max(xi, xi)
        bottom = min(yi, y_pred)
        top = max(yi, y_pred)
        ax3.fill_between([left, right], [bottom, bottom], [top, top],
                         color='green', alpha=0.1)
        ax3.plot([xi, xi], [yi, y_pred], color='green', linestyle='--', alpha=0.3)
    ax3.set_xlabel(x_col)
    ax3.set_ylabel(y_col)
    ax3.set_title('Квадраты ошибок')
    ax3.legend()
    ax3.grid(True)

    plt.tight_layout()  # Чтобы графики не накладывались друг на друга
    plt.show()

def main():
    filename = input("Введите имя CSV файла с данными: ")

    try:
        data = read_data(filename)
        print("Данные успешно загружены:")
        print(data.head())

        print("\nДоступные столбцы:", list(data.columns))
        x_col = input("Выберите столбец для X: ")
        y_col = input("Выберите столбец для Y: ")

        # Проверка наличия столбцов
        if x_col not in data.columns or y_col not in data.columns:
            raise ValueError("Указанные столбцы не найдены в данных")

        # Вывод статистики
        print_statistics(data, x_col, y_col)

        a, b = linear_regression(data[x_col], data[y_col])
        print(f"\nПараметры регрессионной прямой: a = {a:.4f}, b = {b:.4f}")

        plot_all_graphs(data, x_col, y_col, a, b)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
