





import java.util.List;
import java.util.ArrayList;

public class railway_TrackElement extends RailwayElement {






    private List<railway_TrackElement> railway_trackelements;


    public railway_TrackElement(
    ) {
        super(
        );
        this.railway_trackelements = new ArrayList<>();
    }

    public railway_TrackElement(
        ArrayList<railway_TrackElement> railway_trackelements    ) {
        this.railway_trackelements = railway_trackelements;
    }


    public List<railway_TrackElement> getRailway_trackelements() {
        return railway_trackelements;
    }

    public void addRailway_trackelement(Railway_trackelement railway_trackelement) {
        this.railway_trackelements.add(railway_trackelement);
    }

}