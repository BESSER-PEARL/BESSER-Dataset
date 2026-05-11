





import java.util.List;
import java.util.ArrayList;

public class draw2d_PolylineShape extends PointListShape {

    private int tolerance;



    public draw2d_PolylineShape(
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