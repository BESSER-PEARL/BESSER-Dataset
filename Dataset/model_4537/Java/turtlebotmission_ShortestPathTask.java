





import java.util.List;
import java.util.ArrayList;

public class turtlebotmission_ShortestPathTask extends Task {






    private List<turtlebotmission_WayPoint> turtlebotmission_waypoints;


    public turtlebotmission_ShortestPathTask(
    ) {
        super(
        );
        this.turtlebotmission_waypoints = new ArrayList<>();
    }

    public turtlebotmission_ShortestPathTask(
        ArrayList<turtlebotmission_WayPoint> turtlebotmission_waypoints    ) {
        this.turtlebotmission_waypoints = turtlebotmission_waypoints;
    }


    public List<turtlebotmission_WayPoint> getTurtlebotmission_waypoints() {
        return turtlebotmission_waypoints;
    }

    public void addTurtlebotmission_waypoint(Turtlebotmission_waypoint turtlebotmission_waypoint) {
        this.turtlebotmission_waypoints.add(turtlebotmission_waypoint);
    }

}