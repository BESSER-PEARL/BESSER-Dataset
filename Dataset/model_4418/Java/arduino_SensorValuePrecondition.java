





import java.util.List;
import java.util.ArrayList;

public class arduino_SensorValuePrecondition  {

    private String value;
    private String cond;





    private arduino_Sensor arduino_sensor;


    public arduino_SensorValuePrecondition(
        String value,        String cond    ) {
        this.value = value;
        this.cond = cond;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
    }

    public arduino_Sensor getArduino_sensor() {
        return arduino_sensor;
    }

    public void setArduino_sensor(arduino_Sensor arduino_sensor) {
        this.arduino_sensor = arduino_sensor;
    }

}