





import java.util.List;
import java.util.ArrayList;

public class railway_Sensor extends RailwayElement {






    private railway_Route railway_route;




    private railway_Region railway_region;


    public railway_Sensor(
    ) {
        super(
        );
    }



    public railway_Route getRailway_route() {
        return railway_route;
    }

    public void setRailway_route(railway_Route railway_route) {
        this.railway_route = railway_route;
    }
    public railway_Region getRailway_region() {
        return railway_region;
    }

    public void setRailway_region(railway_Region railway_region) {
        this.railway_region = railway_region;
    }

}