





import java.util.List;
import java.util.ArrayList;

public class mindstorms_GoTo extends Action {

    private int y;
    private int x;



    public mindstorms_GoTo(
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