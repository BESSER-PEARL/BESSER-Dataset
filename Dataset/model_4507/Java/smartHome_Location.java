





import java.util.List;
import java.util.ArrayList;

public class smartHome_Location  {

    private String name;





    private List<smartHome_Sensor> smarthome_sensors;


    public smartHome_Location(
        String name    ) {
        this.name = name;
        this.smarthome_sensors = new ArrayList<>();
    }

    public smartHome_Location(
        String name        ArrayList<smartHome_Sensor> smarthome_sensors    ) {
        this.name = name;
        this.smarthome_sensors = smarthome_sensors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<smartHome_Sensor> getSmarthome_sensors() {
        return smarthome_sensors;
    }

    public void addSmarthome_sensor(Smarthome_sensor smarthome_sensor) {
        this.smarthome_sensors.add(smarthome_sensor);
    }

}