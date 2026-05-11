





import java.util.List;
import java.util.ArrayList;

public class smartHome_SensorType  {

    private String name;





    private smartHome_Sensor smarthome_sensor;


    public smartHome_SensorType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smartHome_Sensor getSmarthome_sensor() {
        return smarthome_sensor;
    }

    public void setSmarthome_sensor(smartHome_Sensor smarthome_sensor) {
        this.smarthome_sensor = smarthome_sensor;
    }

}