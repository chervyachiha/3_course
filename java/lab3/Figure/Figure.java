package Figures;

public abstract class Figure {
    private String name;
    private char color;

    public Figure(String name, char color) {
        this.name = name;
        this.color = color;
    }

    public String getName() {
        return name;
    }

    public char getColor() {
        return color;
    }

    public abstract boolean canMove(int row, int col, int row1, int col1);

    public boolean canAttack(int row, int col, int row1, int col1) {
        return canMove(row, col, row1, col1);
    }
}
