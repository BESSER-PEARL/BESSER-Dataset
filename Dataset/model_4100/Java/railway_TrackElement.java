





import java.util.List;
import java.util.ArrayList;

public class railway_TrackElement extends RailwayElement {






    private railway_Switch railway_switch;




    private List<railway_TrackElement> railway_trackelements;




    private railway_Switch railway_switch;




    private railway_Switch railway_switch;




    private railway_Segment railway_segment;


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


    public railway_Switch getRailway_switch() {
        return railway_switch;
    }

    public void setRailway_switch(railway_Switch railway_switch) {
        this.railway_switch = railway_switch;
    }
    public List<railway_TrackElement> getRailway_trackelements() {
        return railway_trackelements;
    }

    public void addRailway_trackelement(Railway_trackelement railway_trackelement) {
        this.railway_trackelements.add(railway_trackelement);
    }
    public railway_Switch getRailway_switch() {
        return railway_switch;
    }

    public void setRailway_switch(railway_Switch railway_switch) {
        this.railway_switch = railway_switch;
    }
    public railway_Switch getRailway_switch() {
        return railway_switch;
    }

    public void setRailway_switch(railway_Switch railway_switch) {
        this.railway_switch = railway_switch;
    }
    public railway_Segment getRailway_segment() {
        return railway_segment;
    }

    public void setRailway_segment(railway_Segment railway_segment) {
        this.railway_segment = railway_segment;
    }

}