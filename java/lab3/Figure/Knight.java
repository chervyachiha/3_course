package Figures;

public class Knight extends Figure {
    public Knight(String name, char color) {
        super(name, color);
    }

    @Override
    public boolean canMove(int row, int col, int row1, int col1) {
        int dx = Math.abs(row - row1);
        int dy = Math.abs(col - col1);
        return dx * dy == 2;
    }
}
