





import java.util.List;
import java.util.ArrayList;

public class vmlogo_Point  {

    private float x;
    private float y;





    private vmlogo_Turtle vmlogo_turtle;


    public vmlogo_Point(
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

    public vmlogo_Turtle getVmlogo_turtle() {
        return vmlogo_turtle;
    }

    public void setVmlogo_turtle(vmlogo_Turtle vmlogo_turtle) {
        this.vmlogo_turtle = vmlogo_turtle;
    }

}