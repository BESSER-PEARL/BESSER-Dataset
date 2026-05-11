





import java.util.List;
import java.util.ArrayList;

public class draw2d_Polyline extends PointListShape {

    private int tolerance;



    public draw2d_Polyline(
        int tolerance    ) {
        super(
        );
        this.tolerance = tolerance;
    }


    public int getTolerance() {
        return tolerance;
    }

    public void setTolerance(int tolerance) {
        this.tolerance = tolerance;
    }


}