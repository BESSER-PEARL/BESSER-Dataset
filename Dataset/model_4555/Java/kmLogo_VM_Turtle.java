





import java.util.List;
import java.util.ArrayList;

public class kmLogo_VM_Turtle  {

    private String penUp;
    private String heading;



    public kmLogo_VM_Turtle(
        String penUp,        String heading    ) {
        this.penUp = penUp;
        this.heading = heading;
    }


    public String getPenup() {
        return penUp;
    }

    public void setPenup(String penUp) {
        this.penUp = penUp;
    }
    public String getHeading() {
        return heading;
    }

    public void setHeading(String heading) {
        this.heading = heading;
    }


}