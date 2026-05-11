





import java.util.List;
import java.util.ArrayList;

public class ioT_SensorGroup  {

    private String name;





    private List<ioT_Sensor> iot_sensors;


    public ioT_SensorGroup(
        String name    ) {
        this.name = name;
        this.iot_sensors = new ArrayList<>();
    }

    public ioT_SensorGroup(
        String name        ArrayList<ioT_Sensor> iot_sensors    ) {
        this.name = name;
        this.iot_sensors = iot_sensors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ioT_Sensor> getIot_sensors() {
        return iot_sensors;
    }

    public void addIot_sensor(Iot_sensor iot_sensor) {
        this.iot_sensors.add(iot_sensor);
    }

}