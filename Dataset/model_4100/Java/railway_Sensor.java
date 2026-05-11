





import java.util.List;
import java.util.ArrayList;

public class railway_Sensor extends RailwayElement {






    private railway_Route railway_route;




    private railway_TrackElement railway_trackelement;




    private List<railway_TrackElement> railway_trackelements;


    public railway_Sensor(
    ) {
        super(
        );
        this.railway_trackelements = new ArrayList<>();
    }

    public railway_Sensor(
        ArrayList<railway_TrackElement> railway_trackelements    ) {
        this.railway_trackelements = railway_trackelements;
    }


    public railway_Route getRailway_route() {
        return railway_route;
    }

    public void setRailway_route(railway_Route railway_route) {
        this.railway_route = railway_route;
    }
    public railway_TrackElement getRailway_trackelement() {
        return railway_trackelement;
    }

    public void setRailway_trackelement(railway_TrackElement railway_trackelement) {
        this.railway_trackelement = railway_trackelement;
    }
    public List<railway_TrackElement> getRailway_trackelements() {
        return railway_trackelements;
    }

    public void addRailway_trackelement(Railway_trackelement railway_trackelement) {
        this.railway_trackelements.add(railway_trackelement);
    }

}