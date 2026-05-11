





import java.util.List;
import java.util.ArrayList;

public class railway_Route extends RailwayElement {

    private boolean active;





    private railway_RailwayContainer railway_railwaycontainer;


    public railway_Route(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public railway_RailwayContainer getRailway_railwaycontainer() {
        return railway_railwaycontainer;
    }

    public void setRailway_railwaycontainer(railway_RailwayContainer railway_railwaycontainer) {
        this.railway_railwaycontainer = railway_railwaycontainer;
    }

}