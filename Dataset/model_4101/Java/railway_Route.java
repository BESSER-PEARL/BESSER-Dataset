





import java.util.List;
import java.util.ArrayList;

public class railway_Route extends RailwayElement {






    private railway_Semaphore railway_semaphore;




    private List<railway_Sensor> railway_sensors;




    private railway_Semaphore railway_semaphore;




    private railway_SwitchPosition railway_switchposition;




    private List<railway_SwitchPosition> railway_switchpositions;


    public railway_Route(
    ) {
        super(
        );
        this.railway_sensors = new ArrayList<>();
        this.railway_switchpositions = new ArrayList<>();
    }

    public railway_Route(
        ArrayList<railway_Sensor> railway_sensors,        ArrayList<railway_SwitchPosition> railway_switchpositions    ) {
        this.railway_sensors = railway_sensors;
        this.railway_switchpositions = railway_switchpositions;
    }


    public railway_Semaphore getRailway_semaphore() {
        return railway_semaphore;
    }

    public void setRailway_semaphore(railway_Semaphore railway_semaphore) {
        this.railway_semaphore = railway_semaphore;
    }
    public List<railway_Sensor> getRailway_sensors() {
        return railway_sensors;
    }

    public void addRailway_sensor(Railway_sensor railway_sensor) {
        this.railway_sensors.add(railway_sensor);
    }
    public railway_Semaphore getRailway_semaphore() {
        return railway_semaphore;
    }

    public void setRailway_semaphore(railway_Semaphore railway_semaphore) {
        this.railway_semaphore = railway_semaphore;
    }
    public railway_SwitchPosition getRailway_switchposition() {
        return railway_switchposition;
    }

    public void setRailway_switchposition(railway_SwitchPosition railway_switchposition) {
        this.railway_switchposition = railway_switchposition;
    }
    public List<railway_SwitchPosition> getRailway_switchpositions() {
        return railway_switchpositions;
    }

    public void addRailway_switchposition(Railway_switchposition railway_switchposition) {
        this.railway_switchpositions.add(railway_switchposition);
    }

}