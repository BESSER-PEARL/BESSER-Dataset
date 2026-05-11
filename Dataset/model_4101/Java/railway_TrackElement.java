





import java.util.List;
import java.util.ArrayList;

public class railway_TrackElement extends RailwayElement {






    private List<railway_Sensor> railway_sensors;




    private railway_Switch railway_switch;




    private railway_TrackElement railway_trackelement;




    private railway_Switch railway_switch;




    private railway_Switch railway_switch;




    private railway_Segment railway_segment;




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


    public List<railway_Sensor> getRailway_sensors() {
        return railway_sensors;
    }

    public void addRailway_sensor(Railway_sensor railway_sensor) {
        this.railway_sensors.add(railway_sensor);
    }
    public railway_Switch getRailway_switch() {
        return railway_switch;
    }

    public void setRailway_switch(railway_Switch railway_switch) {
        this.railway_switch = railway_switch;
    }
    public railway_TrackElement getRailway_trackelement() {
        return railway_trackelement;
    }

    public void setRailway_trackelement(railway_TrackElement railway_trackelement) {
        this.railway_trackelement = railway_trackelement;
    }
    public railway_Switch getRailway_switch() {
        return railway_switch;
    }

    public void setRailway_switch(railway_Switch railway_switch) {
        this.railway_switch = railway_switch;
    }
    public railway_Switch getRailway_switch() {
        return railway_switch;
    }

    public void setRailway_switch(railway_Switch railway_switch) {
        this.railway_switch = railway_switch;
    }
    public railway_Segment getRailway_segment() {
        return railway_segment;
    }

    public void setRailway_segment(railway_Segment railway_segment) {
        this.railway_segment = railway_segment;
    }
    public railway_Sensor getRailway_sensor() {
        return railway_sensor;
    }

    public void setRailway_sensor(railway_Sensor railway_sensor) {
        this.railway_sensor = railway_sensor;
    }

}