





import java.util.List;
import java.util.ArrayList;

public class railway_RailwayContainer  {






    private List<railway_Route> railway_routes;




    private List<railway_Region> railway_regions;


    public railway_RailwayContainer(
    ) {
        this.railway_routes = new ArrayList<>();
        this.railway_regions = new ArrayList<>();
    }

    public railway_RailwayContainer(
        ArrayList<railway_Route> railway_routes,        ArrayList<railway_Region> railway_regions    ) {
        this.railway_routes = railway_routes;
        this.railway_regions = railway_regions;
    }


    public List<railway_Route> getRailway_routes() {
        return railway_routes;
    }

    public void addRailway_route(Railway_route railway_route) {
        this.railway_routes.add(railway_route);
    }
    public List<railway_Region> getRailway_regions() {
        return railway_regions;
    }

    public void addRailway_region(Railway_region railway_region) {
        this.railway_regions.add(railway_region);
    }

}