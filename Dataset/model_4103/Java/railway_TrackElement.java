





import java.util.List;
import java.util.ArrayList;

public class railway_TrackElement extends RailwayElement {






    private railway_Region railway_region;




    private railway_TrackElement railway_trackelement;




    private List<railway_Sensor> railway_sensors;




    private railway_Sensor railway_sensor;


    public railway_TrackElement(
    ) {
        super(
        );
        this.railway_sensors = new ArrayList<>();
    }

    public railway_TrackElement(
        ArrayList<railway_Sensor> railway_sensors    ) {
        this.railway_sensors = railway_sensors;
    }


    public railway_Region getRailway_region() {
        return railway_region;
    }

    public void setRailway_region(railway_Region railway_region) {
        this.railway_region = railway_region;
    }
    public railway_TrackElement getRailway_trackelement() {
        return railway_trackelement;
    }

    public void setRailway_trackelement(railway_TrackElement railway_trackelement) {
        this.railway_trackelement = railway_trackelement;
    }
    public List<railway_Sensor> getRailway_sensors() {
        return railway_sensors;
    }

    public void addRailway_sensor(Railway_sensor railway_sensor) {
        this.railway_sensors.add(railway_sensor);
    }
    public railway_Sensor getRailway_sensor() {
        return railway_sensor;
    }

    public void setRailway_sensor(railway_Sensor railway_sensor) {
        this.railway_sensor = railway_sensor;
    }

}