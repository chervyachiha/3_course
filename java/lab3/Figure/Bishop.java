package Figures;

public class Bishop extends Figure {
    public Bishop(String name, char color) {
        super(name, color);
    }

    @Override
    public boolean canMove(int row, int col, int row1, int col1) {
        return Math.abs(row - row1) == Math.abs(col - col1);
    }
}
