





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Point  {

    private float x;
    private float y;





    private kmLogo_Turtle kmlogo_turtle;


    public kmLogo_Point(
        float x,        float y    ) {
        this.x = x;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public kmLogo_Turtle getKmlogo_turtle() {
        return kmlogo_turtle;
    }

    public void setKmlogo_turtle(kmLogo_Turtle kmlogo_turtle) {
        this.kmlogo_turtle = kmlogo_turtle;
    }

}