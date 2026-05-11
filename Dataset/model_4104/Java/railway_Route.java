





import java.util.List;
import java.util.ArrayList;

public class railway_Route extends RailwayElement {

    private boolean active;





    private railway_Semaphore railway_semaphore;




    private railway_Semaphore railway_semaphore;




    private List<railway_SwitchPosition> railway_switchpositions;




    private railway_SwitchPosition railway_switchposition;




    private railway_RailwayContainer railway_railwaycontainer;


    public railway_Route(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.railway_switchpositions = new ArrayList<>();
    }

    public railway_Route(
        boolean active        ArrayList<railway_SwitchPosition> railway_switchpositions    ) {
        this.active = active;
        this.railway_switchpositions = railway_switchpositions;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public railway_Semaphore getRailway_semaphore() {
        return railway_semaphore;
    }

    public void setRailway_semaphore(railway_Semaphore railway_semaphore) {
        this.railway_semaphore = railway_semaphore;
    }
    public railway_Semaphore getRailway_semaphore() {
        return railway_semaphore;
    }

    public void setRailway_semaphore(railway_Semaphore railway_semaphore) {
        this.railway_semaphore = railway_semaphore;
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
    public railway_RailwayContainer getRailway_railwaycontainer() {
        return railway_railwaycontainer;
    }

    public void setRailway_railwaycontainer(railway_RailwayContainer railway_railwaycontainer) {
        this.railway_railwaycontainer = railway_railwaycontainer;
    }

}