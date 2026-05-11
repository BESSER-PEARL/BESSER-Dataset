





import java.util.List;
import java.util.ArrayList;

public class railway_RailwayContainer  {






    private List<railway_Route> railway_routes;




    private List<railway_Semaphore> railway_semaphores;


    public railway_RailwayContainer(
    ) {
        this.railway_routes = new ArrayList<>();
        this.railway_semaphores = new ArrayList<>();
    }

    public railway_RailwayContainer(
        ArrayList<railway_Route> railway_routes,        ArrayList<railway_Semaphore> railway_semaphores    ) {
        this.railway_routes = railway_routes;
        this.railway_semaphores = railway_semaphores;
    }


    public List<railway_Route> getRailway_routes() {
        return railway_routes;
    }

    public void addRailway_route(Railway_route railway_route) {
        this.railway_routes.add(railway_route);
    }
    public List<railway_Semaphore> getRailway_semaphores() {
        return railway_semaphores;
    }

    public void addRailway_semaphore(Railway_semaphore railway_semaphore) {
        this.railway_semaphores.add(railway_semaphore);
    }

}