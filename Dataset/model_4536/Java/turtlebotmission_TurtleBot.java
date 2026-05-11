





import java.util.List;
import java.util.ArrayList;

public class turtlebotmission_TurtleBot extends NamedElement {






    private List<turtlebotmission_WayPoint> turtlebotmission_waypoints;




    private List<turtlebotmission_Mission> turtlebotmission_missions;




    private turtlebotmission_WayPoint turtlebotmission_waypoint;


    public turtlebotmission_TurtleBot(
    ) {
        super(
        );
        this.turtlebotmission_waypoints = new ArrayList<>();
        this.turtlebotmission_missions = new ArrayList<>();
    }

    public turtlebotmission_TurtleBot(
        ArrayList<turtlebotmission_WayPoint> turtlebotmission_waypoints,        ArrayList<turtlebotmission_Mission> turtlebotmission_missions    ) {
        this.turtlebotmission_waypoints = turtlebotmission_waypoints;
        this.turtlebotmission_missions = turtlebotmission_missions;
    }


    public List<turtlebotmission_WayPoint> getTurtlebotmission_waypoints() {
        return turtlebotmission_waypoints;
    }

    public void addTurtlebotmission_waypoint(Turtlebotmission_waypoint turtlebotmission_waypoint) {
        this.turtlebotmission_waypoints.add(turtlebotmission_waypoint);
    }
    public List<turtlebotmission_Mission> getTurtlebotmission_missions() {
        return turtlebotmission_missions;
    }

    public void addTurtlebotmission_mission(Turtlebotmission_mission turtlebotmission_mission) {
        this.turtlebotmission_missions.add(turtlebotmission_mission);
    }
    public turtlebotmission_WayPoint getTurtlebotmission_waypoint() {
        return turtlebotmission_waypoint;
    }

    public void setTurtlebotmission_waypoint(turtlebotmission_WayPoint turtlebotmission_waypoint) {
        this.turtlebotmission_waypoint = turtlebotmission_waypoint;
    }

}