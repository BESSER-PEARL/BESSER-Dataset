





import java.util.List;
import java.util.ArrayList;

public class door_alarm_system  {

    private boolean door_alarm_system;





    private control_panel control_panel;




    private eventlog eventlog;




    private List<door_sensor> door_sensors;


    public door_alarm_system(
        boolean door_alarm_system    ) {
        this.door_alarm_system = door_alarm_system;
        this.door_sensors = new ArrayList<>();
    }

    public door_alarm_system(
        boolean door_alarm_system        ArrayList<door_sensor> door_sensors    ) {
        this.door_alarm_system = door_alarm_system;
        this.door_sensors = door_sensors;
    }

    public boolean getDoor_alarm_system() {
        return door_alarm_system;
    }

    public void setDoor_alarm_system(boolean door_alarm_system) {
        this.door_alarm_system = door_alarm_system;
    }

    public control_panel getControl_panel() {
        return control_panel;
    }

    public void setControl_panel(control_panel control_panel) {
        this.control_panel = control_panel;
    }
    public eventlog getEventlog() {
        return eventlog;
    }

    public void setEventlog(eventlog eventlog) {
        this.eventlog = eventlog;
    }
    public List<door_sensor> getDoor_sensors() {
        return door_sensors;
    }

    public void addDoor_sensor(Door_sensor door_sensor) {
        this.door_sensors.add(door_sensor);
    }

}