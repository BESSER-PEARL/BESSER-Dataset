





import java.util.List;
import java.util.ArrayList;

public class Field  {

    private int x;
    private None color;
    private int y;



    public Field(
        int x,        None color,        int y    ) {
        this.x = x;
        this.color = color;
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
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }


}