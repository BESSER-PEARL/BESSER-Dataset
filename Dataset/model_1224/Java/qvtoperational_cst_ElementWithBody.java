





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ElementWithBody  {

    private int bodyEndLocation;
    private int bodyStartLocation;



    public qvtoperational_cst_ElementWithBody(
        int bodyEndLocation,        int bodyStartLocation    ) {
        this.bodyEndLocation = bodyEndLocation;
        this.bodyStartLocation = bodyStartLocation;
    }


    public int getBodyendlocation() {
        return bodyEndLocation;
    }

    public void setBodyendlocation(int bodyEndLocation) {
        this.bodyEndLocation = bodyEndLocation;
    }
    public int getBodystartlocation() {
        return bodyStartLocation;
    }

    public void setBodystartlocation(int bodyStartLocation) {
        this.bodyStartLocation = bodyStartLocation;
    }


}