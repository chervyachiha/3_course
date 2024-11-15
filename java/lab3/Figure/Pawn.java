package Figures;

public class Pawn extends Figure {
    private boolean isFirstMove = true;

    public Pawn(String name, char color) {
        super(name, color);
    }

    @Override
    public boolean canMove(int row, int col, int row1, int col1) {
        int direction = (getColor() == 'w') ? 1 : -1; // Направление движения: вверх для белых, вниз для черных

        if (col == col1) {  // Прямое движение
            if (row + direction == row1) {
                isFirstMove = false;  // После первого хода устанавливаем его в false
                return true;
            } else if (isFirstMove && row + 2 * direction == row1) {  // Первый ход на две клетки
                isFirstMove = false;
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean canAttack(int row, int col, int row1, int col1) {
        int direction = (getColor() == 'w') ? 1 : -1;  // Определяем направление атаки
        return (Math.abs(col - col1) == 1 && row + direction == row1);
    }
}
