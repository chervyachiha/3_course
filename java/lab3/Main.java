import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Board board = new Board();
        board.init();
        board.setColorGame('w');

        boolean isGame = true;
        Scanner in = new Scanner(System.in);

        while (isGame) {
            board.print_board();
            System.out.println();

            System.out.println("Управление:");
            System.out.println("----row col row1 col1: Ход фигуры из клетки (row, col) в (row1, col1)");

            switch (board.getColorGame()) {
                case 'w': System.out.println("Ход белых"); break;
                case 'b': System.out.println("Ход черных"); break;
            }

            System.out.print("Введите ход: ");
            try {
                String inputLine = in.nextLine();
                String[] coords = inputLine.split(" ");

                if (coords.length != 4) {
                    System.out.println("Неверный формат ввода! Введите четыре числа через пробел.");
                    continue;
                }

                int row = Integer.parseInt(coords[0]);
                int col = Integer.parseInt(coords[1]);
                int row1 = Integer.parseInt(coords[2]);
                int col1 = Integer.parseInt(coords[3]);

                // Проверка координат на корректность
                if (row < 0 || row > 7 || col < 0 || col > 7 ||
                        row1 < 0 || row1 > 7 || col1 < 0 || col1 > 7) {
                    System.out.println("Координаты должны быть в диапазоне от 0 до 7!");
                    continue;
                }

                if (!board.move_figure(row, col, row1, col1)) {
                    System.out.println("Ошибка! Невозможный ход!");
                    continue;
                }

                // Проверяем шах противнику после хода
                char oppositeColor = (board.getColorGame() == 'w') ? 'b' : 'w';
                if (board.isCheck(oppositeColor)) {
                    if (board.isMate(oppositeColor)) {
                        System.out.println("Мат! Игра окончена.");
                        isGame = false;
                    } else {
                        System.out.println("Шах!");
                    }
                }
                board.switchColor();

            } catch (NumberFormatException e) {
                System.out.println("Ошибка! Введите числовые координаты!");
            } catch (Exception e) {
                System.out.println("Произошла ошибка: " + e.getMessage());
            }
        }
        in.close();
    }
}