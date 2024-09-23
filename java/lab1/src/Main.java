import java.util.Objects;
import java.util.Scanner;
public class Main
{
    private static final Scanner input = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.println("Выбери номер задания\n1)Сиракузская последовательность\n" +
                "2)Сумма ряда\n3)Ищем клад\n4)Логистический максимин\n5)Дважды четное число");
        int a = input.nextInt();
        switch (a){
            case 1:
                posl();
                break;
            case 2:
                summa();
                break;
            case 3:
                klad();
                break;
            case 4:
                logmax();
                break;
            case 5:
                chet();
                break;
        }
    }

    static void posl()
    {
        int n = input.nextInt();
        int k = 0;
        while (n!=1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            k += 1;
        }
        System.out.println(k);
    }

    static void summa()
    {
        int n = input.nextInt();
        int k =0;
        int[] mas = new int[n];
        for (int i = 0; i < n; i++) {
            mas[i] = input.nextInt();
        }
        for (int i = 0; i < n; i++) {
            if (i%2==1)
            {
                k-=mas[i];
            }
            else
            {
                k+=mas[i];
            }
        }
        System.out.println(k);
    }

    static void klad()
    {
        int x0 = input.nextInt();
        int y0 = input.nextInt();
        String direction = input.next();
        int n;
        int x = 0;
        int y = 0;
        int counter = 0;
        int count = Integer.MAX_VALUE;
        while (!Objects.equals(direction, "стоп")) {
            n = input.nextInt();
            if (direction.equals("север")) {
                y += n;
                counter += 1;
            }
            if (direction.equals("юг")) {
                y -= n;
                counter += 1;
            }
            if (direction.equals("запад")) {
                x -= n;
                counter += 1;
            }
            if (direction.equals("восток")) {
                x += n;
                counter += 1;
            }
            if (x==x0 && y==y0) {
                if (counter<count)
                {
                    count = counter;
                }
            }
            direction = input.next();
        }
        System.out.println(count);
    }


    static void logmax()
    {
        int n = input.nextInt();
        int[] mas = new int[n];
        for (int i = 0; i < n; i++) {
            int k = input.nextInt();
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < k; j++) {
                int m = input.nextInt();
                if (min > m) {
                    min = m;
                }
            }
            mas[i] = min;
        }
        int max = Integer.MIN_VALUE;
        int l = 0;
        for (int i = 0; i < n; i++) {
            if (max < mas[i]) {
                max = mas[i];
                l = i + 1;
            }
        }
        System.out.println(l + " " + max);
    }

    static void chet()
    {
        int n = input.nextInt();
        int sum = 0;
        int pr; // = 1;
        int[] mas = new int[3];
        for (int i = 2; i >= 0; i--) {
            mas[i] = n%10;
            n/=10;
        }
        pr = mas[0]*mas[1]*mas[2];
        sum = mas[0]+mas[1]+mas[2];
        if (sum%2==0 & pr%2==0) {
            System.out.println("Дважды четное");
        }
        else {
            System.out.println("Не дважды четное");
        }




    }
}