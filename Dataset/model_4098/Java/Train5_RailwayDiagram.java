





import java.util.List;
import java.util.ArrayList;

public class Train5_RailwayDiagram  {






    private List<Train5_SensorNetwork> train5_sensornetworks;




    private List<Train5_Route> train5_routes;




    private List<Train5_TrackElement> train5_trackelements;


    public Train5_RailwayDiagram(
    ) {
        this.train5_sensornetworks = new ArrayList<>();
        this.train5_routes = new ArrayList<>();
        this.train5_trackelements = new ArrayList<>();
    }

    public Train5_RailwayDiagram(
        ArrayList<Train5_SensorNetwork> train5_sensornetworks,        ArrayList<Train5_Route> train5_routes,        ArrayList<Train5_TrackElement> train5_trackelements    ) {
        this.train5_sensornetworks = train5_sensornetworks;
        this.train5_routes = train5_routes;
        this.train5_trackelements = train5_trackelements;
    }


    public List<Train5_SensorNetwork> getTrain5_sensornetworks() {
        return train5_sensornetworks;
    }

    public void addTrain5_sensornetwork(Train5_sensornetwork train5_sensornetwork) {
        this.train5_sensornetworks.add(train5_sensornetwork);
    }
    public List<Train5_Route> getTrain5_routes() {
        return train5_routes;
    }

    public void addTrain5_route(Train5_route train5_route) {
        this.train5_routes.add(train5_route);
    }
    public List<Train5_TrackElement> getTrain5_trackelements() {
        return train5_trackelements;
    }

    public void addTrain5_trackelement(Train5_trackelement train5_trackelement) {
        this.train5_trackelements.add(train5_trackelement);
    }

}