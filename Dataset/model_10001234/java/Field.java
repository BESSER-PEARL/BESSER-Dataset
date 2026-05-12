





import java.util.List;
import java.util.ArrayList;

public class Field  {

    private None color;
    private int y;
    private int x;



    public Field(
        None color,        int y,        int x    ) {
        this.color = color;
        this.y = y;
        this.x = x;
    }


    public None getColor() {
        return color;
    }

    public void setColor(None color) {
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


}