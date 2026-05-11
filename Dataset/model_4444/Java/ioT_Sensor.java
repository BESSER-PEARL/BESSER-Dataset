





import java.util.List;
import java.util.ArrayList;

public class ioT_Sensor  {

    private String name;





    private ioT_SensorType iot_sensortype;


    public ioT_Sensor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_SensorType getIot_sensortype() {
        return iot_sensortype;
    }

    public void setIot_sensortype(ioT_SensorType iot_sensortype) {
        this.iot_sensortype = iot_sensortype;
    }

}