





import java.util.List;
import java.util.ArrayList;

public class vmlogo_Turtle  {

    private boolean penUp;
    private float heading;





    private List<vmlogo_Segment> vmlogo_segments;


    public vmlogo_Turtle(
        boolean penUp,        float heading    ) {
        this.penUp = penUp;
        this.heading = heading;
        this.vmlogo_segments = new ArrayList<>();
    }

    public vmlogo_Turtle(
        boolean penUp,        float heading        ArrayList<vmlogo_Segment> vmlogo_segments    ) {
        this.penUp = penUp;
        this.heading = heading;
        this.vmlogo_segments = vmlogo_segments;
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

    public List<vmlogo_Segment> getVmlogo_segments() {
        return vmlogo_segments;
    }

    public void addVmlogo_segment(Vmlogo_segment vmlogo_segment) {
        this.vmlogo_segments.add(vmlogo_segment);
    }

}