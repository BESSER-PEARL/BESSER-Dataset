





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_Candy  {

    private int row;
    private int color;
    private int col;





    private List<candyCrushPackage_Candy> candycrushpackage_candys;


    public candyCrushPackage_Candy(
        int row,        int color,        int col    ) {
        this.row = row;
        this.color = color;
        this.col = col;
        this.candycrushpackage_candys = new ArrayList<>();
    }

    public candyCrushPackage_Candy(
        int row,        int color,        int col        ArrayList<candyCrushPackage_Candy> candycrushpackage_candys    ) {
        this.row = row;
        this.color = color;
        this.col = col;
        this.candycrushpackage_candys = candycrushpackage_candys;
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }
    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }
    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }

    public List<candyCrushPackage_Candy> getCandycrushpackage_candys() {
        return candycrushpackage_candys;
    }

    public void addCandycrushpackage_candy(Candycrushpackage_candy candycrushpackage_candy) {
        this.candycrushpackage_candys.add(candycrushpackage_candy);
    }

}