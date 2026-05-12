





import java.util.List;
import java.util.ArrayList;

public class flood_alarm_system  {

    private boolean flood_alarm_system;





    private control_panel control_panel;




    private eventlog eventlog;




    private List<flood_sensor> flood_sensors;


    public flood_alarm_system(
        boolean flood_alarm_system    ) {
        this.flood_alarm_system = flood_alarm_system;
        this.flood_sensors = new ArrayList<>();
    }

    public flood_alarm_system(
        boolean flood_alarm_system        ArrayList<flood_sensor> flood_sensors    ) {
        this.flood_alarm_system = flood_alarm_system;
        this.flood_sensors = flood_sensors;
    }

    public boolean getFlood_alarm_system() {
        return flood_alarm_system;
    }

    public void setFlood_alarm_system(boolean flood_alarm_system) {
        this.flood_alarm_system = flood_alarm_system;
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
    public List<flood_sensor> getFlood_sensors() {
        return flood_sensors;
    }

    public void addFlood_sensor(Flood_sensor flood_sensor) {
        this.flood_sensors.add(flood_sensor);
    }

}