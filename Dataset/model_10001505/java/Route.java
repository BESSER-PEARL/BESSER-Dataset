





import java.util.List;
import java.util.ArrayList;

public class Route  {

    private String routeName;
    private String stations;
    private String waypoints;
    private String uid;
    private None overviewPolyline;



    public Route(
        String routeName,        String stations,        String waypoints,        String uid,        None overviewPolyline    ) {
        this.routeName = routeName;
        this.stations = stations;
        this.waypoints = waypoints;
        this.uid = uid;
        this.overviewPolyline = overviewPolyline;
    }


    public String getRoutename() {
        return routeName;
    }

    public void setRoutename(String routeName) {
        this.routeName = routeName;
    }
    public String getStations() {
        return stations;
    }

    public void setStations(String stations) {
        this.stations = stations;
    }
    public String getWaypoints() {
        return waypoints;
    }

    public void setWaypoints(String waypoints) {
        this.waypoints = waypoints;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public None getOverviewpolyline() {
        return overviewPolyline;
    }

    public void setOverviewpolyline(None overviewPolyline) {
        this.overviewPolyline = overviewPolyline;
    }


}