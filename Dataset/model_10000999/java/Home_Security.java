





import java.util.List;
import java.util.ArrayList;

public class Home_Security  {






    private List<Event_Log> event_logs;




    private List<Light_Sensor> light_sensors;




    private List<Temperature_sensor> temperature_sensors;




    private Lock_doors_sensors lock_doors_sensors;




    private List<Camera_sensor> camera_sensors;




    private Server server;


    public Home_Security(
    ) {
        this.event_logs = new ArrayList<>();
        this.light_sensors = new ArrayList<>();
        this.temperature_sensors = new ArrayList<>();
        this.camera_sensors = new ArrayList<>();
    }

    public Home_Security(
        ArrayList<Event_Log> event_logs,        ArrayList<Light_Sensor> light_sensors,        ArrayList<Temperature_sensor> temperature_sensors,        ArrayList<Camera_sensor> camera_sensors    ) {
        this.event_logs = event_logs;
        this.light_sensors = light_sensors;
        this.temperature_sensors = temperature_sensors;
        this.camera_sensors = camera_sensors;
    }


    public List<Event_Log> getEvent_logs() {
        return event_logs;
    }

    public void addEvent_log(Event_log event_log) {
        this.event_logs.add(event_log);
    }
    public List<Light_Sensor> getLight_sensors() {
        return light_sensors;
    }

    public void addLight_sensor(Light_sensor light_sensor) {
        this.light_sensors.add(light_sensor);
    }
    public List<Temperature_sensor> getTemperature_sensors() {
        return temperature_sensors;
    }

    public void addTemperature_sensor(Temperature_sensor temperature_sensor) {
        this.temperature_sensors.add(temperature_sensor);
    }
    public Lock_doors_sensors getLock_doors_sensors() {
        return lock_doors_sensors;
    }

    public void setLock_doors_sensors(Lock_doors_sensors lock_doors_sensors) {
        this.lock_doors_sensors = lock_doors_sensors;
    }
    public List<Camera_sensor> getCamera_sensors() {
        return camera_sensors;
    }

    public void addCamera_sensor(Camera_sensor camera_sensor) {
        this.camera_sensors.add(camera_sensor);
    }
    public Server getServer() {
        return server;
    }

    public void setServer(Server server) {
        this.server = server;
    }

}