





import java.util.List;
import java.util.ArrayList;

public class Coordinate  {

    private int x;
    private int y;
    private None state;



    public Coordinate(
        int x,        int y,        None state    ) {
        this.x = x;
        this.y = y;
        this.state = state;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }


}