import java.util.Scanner;
import java.util.HashMap;
import java.util.Arrays;
public class Main
{
    private static final Scanner input = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.println("Выбери номер задания\n1)Наибольшая подстрока\n" +
                "2)Объединение массивов\n" +
                "3)Максимальная сумма\n" +
                "4)Поворот по часовой\n" +
                "5)Заданная сумма\n" +
                "6)Сумма всех элементов\n" +
                "7)Максимальный элемент\n" +
                "8)Поворот против часовой\n");
        int a = input.nextInt();
        switch (a){
            case 1:
                substring();
                break;
            case 2:
                sorted();
                break;
            case 3:
                maxsumma();
                break;
            case 4:
                clockwise();
                break;
            case 5:
                summa();
                break;
            case 6:
                allsumma();
                break;
            case 7:
                maxelement();
                break;
            case 8:
                counterclockwise();
                break;
        }
    }

    static void substring()
    {
        String s = input.nextLine();
        HashMap<Character, Integer> charIndexMap = new HashMap<>();
        int left = 0;
        int maxLength = 0;
        String longestSubstring = "";

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // Если символ уже встречался, передвигаем левую границу
            if (charIndexMap.containsKey(currentChar)) {
                left = Math.max(charIndexMap.get(currentChar) + 1, left);
            }

            // Обновляем индекс текущего символа
            charIndexMap.put(currentChar, right);

            // Проверяем длину текущей подстроки
            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
                longestSubstring = s.substring(left, right + 1);
            }
        }
        System.out.println(longestSubstring);
    }

    static void sorted()
    {
        System.out.println("количество:");
        int n1 = input.nextInt();
        int[] array1 = new int[n1];
        System.out.println("элементы первого массива:");
        for (int i = 0; i < n1; i++) {
            array1[i] = input.nextInt();
        }
        System.out.println("количество:");
        int n2 = input.nextInt();
        int[] array2 = new int[n2];
        System.out.println("элементы второго массива:");
        for (int i = 0; i < n1; i++) {
            array2[i] = input.nextInt();
        }

        int[] mergedArray = new int[array1.length + array2.length];
        int i = 0, j = 0, k = 0;

        while (i < array1.length && j < array2.length) {
            mergedArray[k++] = (array1[i] <= array2[j]) ? array1[i++] : array2[j++];
        }

        while (i < array1.length) {
            mergedArray[k++] = array1[i++];
        }

        while (j < array2.length) {
            mergedArray[k++] = array2[j++];
        }

        System.out.println("Объединенный массив: " + Arrays.toString(mergedArray));

    }

    static void maxsumma()
    {
        System.out.println("количество:");
        int n1 = input.nextInt();
        int[] nums = new int[n1];
        System.out.println("элементы массива:");
        for (int i = 0; i < n1; i++) {
            nums[i] = input.nextInt();
        }

        int maxSum = nums[0];
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        System.out.println("Максимальная сумма подмассива: " + maxSum);
    }

    static void clockwise()
    {
        System.out.println("количество строк:");
        int m = input.nextInt();
        System.out.println("количество столбцов:");
        int n = input.nextInt();
        int[][] matrix = new int[m][n];
        System.out.println("Введите элементы матрицы:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = input.nextInt();
            }
        }
        int[][] rotated = new int[n][m];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                rotated[j][i] = matrix[m-i-1][j];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(rotated[i][j] + " ");
            }
            System.out.println();
        }
    }

    static void summa()
    {
        System.out.println("target:");
        int target = input.nextInt();
        System.out.println("количество:");
        int n1 = input.nextInt();
        int[] nums = new int[n1];
        System.out.println("элементы массива:");
        for (int i = 0; i < n1; i++) {
            nums[i] = input.nextInt();
        }
        int[] summa = {0,0};
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    summa[0] = nums[i];
                    summa[1] = nums[j];
                }
            }
        }

        if (summa[0]!= 0 && summa[1] != 0) {
            System.out.println("Найдена пара: " + summa[0] + ", " + summa[1]);
        } else {
            System.out.println("Пара не найдена.");
    }
    }

    static void allsumma()
    {
        System.out.println("количество строк:");
        int m = input.nextInt();
        System.out.println("количество столбцов:");
        int n = input.nextInt();
        int[][] matrix = new int[m][n];
        System.out.println("Введите элементы матрицы:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = input.nextInt();
            }
        }
        int sum = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sum += matrix[i][j];
            }
        }
        System.out.println(sum);
    }

    static void maxelement()
    {
        System.out.println("количество строк:");
        int m = input.nextInt();
        System.out.println("количество столбцов:");
        int n = input.nextInt();
        int[][] matrix = new int[m][n];
        System.out.println("Введите элементы матрицы:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = input.nextInt();
            }
        }

        int[] maxValues = new int[matrix.length];

        for (int i = 0; i < m; i++) {
            int max = matrix[i][0];
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] > max) {
                    max = matrix[i][j];
                }
            }
            maxValues[i] = max;
        }
        for (int i = 0; i < maxValues.length; i++) {
            System.out.println(maxValues[i]);
    }

}

    static void counterclockwise()
    {
        System.out.println("количество строк:");
        int m = input.nextInt();
        System.out.println("количество столбцов:");
        int n = input.nextInt();
        int[][] matrix = new int[m][n];
        System.out.println("Введите элементы матрицы:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = input.nextInt();
            }
        }
        int[][] rotated = new int[n][m];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                rotated[j][i] = matrix[i][n-j-1];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(rotated[i][j] + " ");
            }
            System.out.println();
        }
    }
}