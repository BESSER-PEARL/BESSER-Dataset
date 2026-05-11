





import java.util.List;
import java.util.ArrayList;

public class model_Point extends Feature {

    private int y;
    private int x;



    public model_Point(
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