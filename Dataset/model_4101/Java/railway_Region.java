





import java.util.List;
import java.util.ArrayList;

public class railway_Region extends RailwayElement {






    private List<railway_Sensor> railway_sensors;




    private List<railway_TrackElement> railway_trackelements;


    public railway_Region(
    ) {
        super(
        );
        this.railway_sensors = new ArrayList<>();
        this.railway_trackelements = new ArrayList<>();
    }

    public railway_Region(
        ArrayList<railway_Sensor> railway_sensors,        ArrayList<railway_TrackElement> railway_trackelements    ) {
        this.railway_sensors = railway_sensors;
        this.railway_trackelements = railway_trackelements;
    }


    public List<railway_Sensor> getRailway_sensors() {
        return railway_sensors;
    }

    public void addRailway_sensor(Railway_sensor railway_sensor) {
        this.railway_sensors.add(railway_sensor);
    }
    public List<railway_TrackElement> getRailway_trackelements() {
        return railway_trackelements;
    }

    public void addRailway_trackelement(Railway_trackelement railway_trackelement) {
        this.railway_trackelements.add(railway_trackelement);
    }

}