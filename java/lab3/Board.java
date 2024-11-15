import Figures.*;

public class Board {
    private char colorGame;
    private Figure[][] fields = new Figure[8][8];

    public void setColorGame(char colorGame) {
        this.colorGame = colorGame;
    }

    public char getColorGame() {
        return colorGame;
    }

    public void switchColor() {
        this.colorGame = (this.colorGame == 'w') ? 'b' : 'w';
    }

    public void init() {
        // Инициализация пешек
        for (int i = 0; i < 8; i++) {
            fields[1][i] = new Pawn("P", 'w');
            fields[6][i] = new Pawn("P", 'b');
        }
        // Инициализация остальных фигур
        fields[0][0] = new Rook("R", 'w'); fields[0][7] = new Rook("R", 'w');
        fields[7][0] = new Rook("R", 'b'); fields[7][7] = new Rook("R", 'b');
        fields[0][1] = new Knight("N", 'w'); fields[0][6] = new Knight("N", 'w');
        fields[7][1] = new Knight("N", 'b'); fields[7][6] = new Knight("N", 'b');
        fields[0][2] = new Bishop("B", 'w'); fields[0][5] = new Bishop("B", 'w');
        fields[7][2] = new Bishop("B", 'b'); fields[7][5] = new Bishop("B", 'b');
        fields[0][3] = new King("K", 'w');
        fields[7][3] = new King("K", 'b');
        fields[0][4] = new Queen("Q", 'w');
        fields[7][4] = new Queen("Q", 'b');
    }

    public String getCell(int row, int col) {
        Figure figure = fields[row][col];
        if (figure == null) {
            return "    ";
        }
        return " " + figure.getColor() + figure.getName() + " ";
    }

    public void print_board() {
        System.out.println(" +----+----+----+----+----+----+----+----+");
        for (int row = 7; row >= 0; row--) {
            System.out.print(row);
            for (int col = 0; col < 8; col++) {
                System.out.print("|" + getCell(row, col));
            }
            System.out.println("|");
            System.out.println(" +----+----+----+----+----+----+----+----+");
        }
        System.out.println("    0    1    2    3    4    5    6    7 ");
    }

    public boolean move_figure(int row, int col, int row1, int col1) {
        Figure figure = fields[row][col];
        // Проверяем, существует ли фигура и правильный ли цвет
        if (figure == null || figure.getColor() != colorGame) return false;

        // Проверяем возможность хода и чистоту пути
        if (figure.canMove(row, col, row1, col1) && isPathClear(row, col, row1, col1)) {
            // Проверяем, не атакуем ли мы своего короля или фигуру своего цвета
            Figure target = fields[row1][col1];
            if (target != null && target.getColor() == colorGame) {
                return false;
            }

            // Временно делаем ход
            fields[row1][col1] = figure;
            fields[row][col] = null;

            // Проверяем, не подставляем ли мы под шах своего короля
            if (isCheck(colorGame)) {
                // Если да - отменяем ход
                fields[row][col] = figure;
                fields[row1][col1] = target;
                return false;
            }
            return true;
        }
        return false;
    }

    public boolean isCheck(char kingColor) {
        // Находим позицию короля
        int kingRow = -1, kingCol = -1;
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Figure figure = fields[row][col];
                if (figure instanceof King && figure.getColor() == kingColor) {
                    kingRow = row;
                    kingCol = col;
                    break;
                }
            }
            if (kingRow != -1) break;
        }

        // Проверяем все фигуры противника
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Figure figure = fields[row][col];
                if (figure != null && figure.getColor() != kingColor) {
                    if (figure.canMove(row, col, kingRow, kingCol) &&
                            isPathClear(row, col, kingRow, kingCol)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean isMate(char kingColor) {
        if (!isCheck(kingColor)) return false;

        // Проверяем все возможные ходы всех фигур
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Figure figure = fields[row][col];
                if (figure != null && figure.getColor() == kingColor) {
                    // Проверяем все возможные клетки для хода
                    for (int newRow = 0; newRow < 8; newRow++) {
                        for (int newCol = 0; newCol < 8; newCol++) {
                            // Пропускаем клетки с фигурами своего цвета
                            if (fields[newRow][newCol] != null &&
                                    fields[newRow][newCol].getColor() == kingColor) {
                                continue;
                            }

                            if (figure.canMove(row, col, newRow, newCol) &&
                                    isPathClear(row, col, newRow, newCol)) {

                                // Пробуем сделать ход
                                Figure target = fields[newRow][newCol];
                                fields[newRow][newCol] = figure;
                                fields[row][col] = null;

                                boolean stillInCheck = isCheck(kingColor);

                                // Возвращаем фигуры обратно
                                fields[row][col] = figure;
                                fields[newRow][newCol] = target;

                                // Если нашёлся ход, спасающий от шаха
                                if (!stillInCheck) return false;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }

    private boolean isPathClear(int row, int col, int row1, int col1) {
        // Для коня путь всегда чист
        if (fields[row][col] instanceof Knight) return true;

        int deltaRow = Integer.signum(row1 - row);
        int deltaCol = Integer.signum(col1 - col);

        int currRow = row + deltaRow;
        int currCol = col + deltaCol;

        while (currRow != row1 || currCol != col1) {
            if (fields[currRow][currCol] != null) return false;
            currRow += deltaRow;
            currCol += deltaCol;
        }
        return true;
    }
}