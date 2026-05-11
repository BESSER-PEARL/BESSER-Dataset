





import java.util.List;
import java.util.ArrayList;

public class railway_RailwayElement  {

    private int id;





    private railway_RailwayContainer railway_railwaycontainer;


    public railway_RailwayElement(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public railway_RailwayContainer getRailway_railwaycontainer() {
        return railway_railwaycontainer;
    }

    public void setRailway_railwaycontainer(railway_RailwayContainer railway_railwaycontainer) {
        this.railway_railwaycontainer = railway_railwaycontainer;
    }

}