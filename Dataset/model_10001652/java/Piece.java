





import java.util.List;
import java.util.ArrayList;

public class Piece  {

    private int y;
    private int x;
    private None color;



    public Piece(
        int y,        int x,        None color    ) {
        this.y = y;
        this.x = x;
        this.color = color;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public None getColor() {
        return color;
    }

    public void setColor(None color) {
        this.color = color;
    }


}