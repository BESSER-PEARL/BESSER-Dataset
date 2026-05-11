





import java.util.List;
import java.util.ArrayList;

public class vmlogo_Turtle  {

    private float heading;
    private boolean penUp;





    private vmlogo_Context vmlogo_context;


    public vmlogo_Turtle(
        float heading,        boolean penUp    ) {
        this.heading = heading;
        this.penUp = penUp;
    }


    public float getHeading() {
        return heading;
    }

    public void setHeading(float heading) {
        this.heading = heading;
    }
    public boolean getPenup() {
        return penUp;
    }

    public void setPenup(boolean penUp) {
        this.penUp = penUp;
    }

    public vmlogo_Context getVmlogo_context() {
        return vmlogo_context;
    }

    public void setVmlogo_context(vmlogo_Context vmlogo_context) {
        this.vmlogo_context = vmlogo_context;
    }

}