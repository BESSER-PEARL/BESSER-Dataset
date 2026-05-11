





import java.util.List;
import java.util.ArrayList;

public class turtlebotmission_WayPoint extends NamedElement {

    private int coord_y;
    private int coord_x;



    public turtlebotmission_WayPoint(
        int coord_y,        int coord_x    ) {
        super(
        );
        this.coord_y = coord_y;
        this.coord_x = coord_x;
    }


    public int getCoord_y() {
        return coord_y;
    }

    public void setCoord_y(int coord_y) {
        this.coord_y = coord_y;
    }
    public int getCoord_x() {
        return coord_x;
    }

    public void setCoord_x(int coord_x) {
        this.coord_x = coord_x;
    }


}