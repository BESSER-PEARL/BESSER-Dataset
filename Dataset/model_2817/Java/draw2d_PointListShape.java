





import java.util.List;
import java.util.ArrayList;

public class draw2d_PointListShape extends Shape {

    private int pointList;



    public draw2d_PointListShape(
        int pointList    ) {
        super(
        );
        this.pointList = pointList;
    }


    public int getPointlist() {
        return pointList;
    }

    public void setPointlist(int pointList) {
        this.pointList = pointList;
    }


}