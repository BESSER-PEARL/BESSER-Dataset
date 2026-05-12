





import java.util.List;
import java.util.ArrayList;

public class fire_alarm_system  {

    private boolean fire_alarm_system_on;





    private List<smoke_sensor> smoke_sensors;




    private eventlog eventlog;




    private List<temp_sensor> temp_sensors;




    private control_panel control_panel;




    private fire_alarm_system fire_alarm_system;


    public fire_alarm_system(
        boolean fire_alarm_system_on    ) {
        this.fire_alarm_system_on = fire_alarm_system_on;
        this.smoke_sensors = new ArrayList<>();
        this.temp_sensors = new ArrayList<>();
    }

    public fire_alarm_system(
        boolean fire_alarm_system_on        ArrayList<smoke_sensor> smoke_sensors,        ArrayList<temp_sensor> temp_sensors    ) {
        this.fire_alarm_system_on = fire_alarm_system_on;
        this.smoke_sensors = smoke_sensors;
        this.temp_sensors = temp_sensors;
    }

    public boolean getFire_alarm_system_on() {
        return fire_alarm_system_on;
    }

    public void setFire_alarm_system_on(boolean fire_alarm_system_on) {
        this.fire_alarm_system_on = fire_alarm_system_on;
    }

    public List<smoke_sensor> getSmoke_sensors() {
        return smoke_sensors;
    }

    public void addSmoke_sensor(Smoke_sensor smoke_sensor) {
        this.smoke_sensors.add(smoke_sensor);
    }
    public eventlog getEventlog() {
        return eventlog;
    }

    public void setEventlog(eventlog eventlog) {
        this.eventlog = eventlog;
    }
    public List<temp_sensor> getTemp_sensors() {
        return temp_sensors;
    }

    public void addTemp_sensor(Temp_sensor temp_sensor) {
        this.temp_sensors.add(temp_sensor);
    }
    public control_panel getControl_panel() {
        return control_panel;
    }

    public void setControl_panel(control_panel control_panel) {
        this.control_panel = control_panel;
    }
    public fire_alarm_system getFire_alarm_system() {
        return fire_alarm_system;
    }

    public void setFire_alarm_system(fire_alarm_system fire_alarm_system) {
        this.fire_alarm_system = fire_alarm_system;
    }

}