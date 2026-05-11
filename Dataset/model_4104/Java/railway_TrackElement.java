





import java.util.List;
import java.util.ArrayList;

public class railway_TrackElement extends RailwayElement {






    private List<railway_TrackElement> railway_trackelements;




    private railway_Region railway_region;




    private railway_Sensor railway_sensor;




    private List<railway_Sensor> railway_sensors;


    public railway_TrackElement(
    ) {
        super(
        );
        this.railway_trackelements = new ArrayList<>();
        this.railway_sensors = new ArrayList<>();
    }

    public railway_TrackElement(
        ArrayList<railway_TrackElement> railway_trackelements,        ArrayList<railway_Sensor> railway_sensors    ) {
        this.railway_trackelements = railway_trackelements;
        this.railway_sensors = railway_sensors;
    }


    public List<railway_TrackElement> getRailway_trackelements() {
        return railway_trackelements;
    }

    public void addRailway_trackelement(Railway_trackelement railway_trackelement) {
        this.railway_trackelements.add(railway_trackelement);
    }
    public railway_Region getRailway_region() {
        return railway_region;
    }

    public void setRailway_region(railway_Region railway_region) {
        this.railway_region = railway_region;
    }
    public railway_Sensor getRailway_sensor() {
        return railway_sensor;
    }

    public void setRailway_sensor(railway_Sensor railway_sensor) {
        this.railway_sensor = railway_sensor;
    }
    public List<railway_Sensor> getRailway_sensors() {
        return railway_sensors;
    }

    public void addRailway_sensor(Railway_sensor railway_sensor) {
        this.railway_sensors.add(railway_sensor);
    }

}