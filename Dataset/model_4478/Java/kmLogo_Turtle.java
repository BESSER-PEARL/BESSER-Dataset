





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Turtle  {

    private boolean penUp;
    private float heading;



    public kmLogo_Turtle(
        boolean penUp,        float heading    ) {
        this.penUp = penUp;
        this.heading = heading;
    }


    public boolean getPenup() {
        return penUp;
    }

    public void setPenup(boolean penUp) {
        this.penUp = penUp;
    }
    public float getHeading() {
        return heading;
    }

    public void setHeading(float heading) {
        this.heading = heading;
    }


}