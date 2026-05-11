





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Point  {

    private boolean yrelative;
    private boolean xrelative;
    private float y;
    private float x;



    public sofiagraphics_Point(
        boolean yrelative,        boolean xrelative,        float y,        float x    ) {
        this.yrelative = yrelative;
        this.xrelative = xrelative;
        this.y = y;
        this.x = x;
    }


    public boolean getYrelative() {
        return yrelative;
    }

    public void setYrelative(boolean yrelative) {
        this.yrelative = yrelative;
    }
    public boolean getXrelative() {
        return xrelative;
    }

    public void setXrelative(boolean xrelative) {
        this.xrelative = xrelative;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }


}