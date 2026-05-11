





import java.util.List;
import java.util.ArrayList;

public class turtlebotmission_WayPoint extends NamedElement {

    private int coord_y;
    private int coord_x;





    private List<turtlebotmission_WaypointType> turtlebotmission_waypointtypes;


    public turtlebotmission_WayPoint(
        int coord_y,        int coord_x    ) {
        super(
        );
        this.coord_y = coord_y;
        this.coord_x = coord_x;
        this.turtlebotmission_waypointtypes = new ArrayList<>();
    }

    public turtlebotmission_WayPoint(
        int coord_y,        int coord_x        ArrayList<turtlebotmission_WaypointType> turtlebotmission_waypointtypes    ) {
        this.coord_y = coord_y;
        this.coord_x = coord_x;
        this.turtlebotmission_waypointtypes = turtlebotmission_waypointtypes;
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

    public List<turtlebotmission_WaypointType> getTurtlebotmission_waypointtypes() {
        return turtlebotmission_waypointtypes;
    }

    public void addTurtlebotmission_waypointtype(Turtlebotmission_waypointtype turtlebotmission_waypointtype) {
        this.turtlebotmission_waypointtypes.add(turtlebotmission_waypointtype);
    }

}