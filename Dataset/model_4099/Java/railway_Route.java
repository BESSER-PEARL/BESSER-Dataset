





import java.util.List;
import java.util.ArrayList;

public class railway_Route extends RailwayElement {






    private List<railway_SwitchPosition> railway_switchpositions;




    private railway_SwitchPosition railway_switchposition;


    public railway_Route(
    ) {
        super(
        );
        this.railway_switchpositions = new ArrayList<>();
    }

    public railway_Route(
        ArrayList<railway_SwitchPosition> railway_switchpositions    ) {
        this.railway_switchpositions = railway_switchpositions;
    }


    public List<railway_SwitchPosition> getRailway_switchpositions() {
        return railway_switchpositions;
    }

    public void addRailway_switchposition(Railway_switchposition railway_switchposition) {
        this.railway_switchpositions.add(railway_switchposition);
    }
    public railway_SwitchPosition getRailway_switchposition() {
        return railway_switchposition;
    }

    public void setRailway_switchposition(railway_SwitchPosition railway_switchposition) {
        this.railway_switchposition = railway_switchposition;
    }

}