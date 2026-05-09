





import java.util.List;
import java.util.ArrayList;

public class notation_AbsoluteBendPoint extends BendPoint {

    private int y;
    private int x;



    public notation_AbsoluteBendPoint(
        int y,        int x    ) {
        super(
        );
        this.y = y;
        this.x = x;
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