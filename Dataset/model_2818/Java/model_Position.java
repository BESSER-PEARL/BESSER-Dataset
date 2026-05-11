





import java.util.List;
import java.util.ArrayList;

public class model_Position extends Feature {

    private boolean xRelative;
    private boolean yRelative;
    private int y;
    private int x;



    public model_Position(
        boolean xRelative,        boolean yRelative,        int y,        int x    ) {
        super(
        );
        this.xRelative = xRelative;
        this.yRelative = yRelative;
        this.y = y;
        this.x = x;
    }


    public boolean getXrelative() {
        return xRelative;
    }

    public void setXrelative(boolean xRelative) {
        this.xRelative = xRelative;
    }
    public boolean getYrelative() {
        return yRelative;
    }

    public void setYrelative(boolean yRelative) {
        this.yRelative = yRelative;
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