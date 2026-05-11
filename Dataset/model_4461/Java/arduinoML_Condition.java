





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Condition  {

    private int analogvalue;
    private String value;
    private String comparator;





    private arduinoML_Sensor arduinoml_sensor;


    public arduinoML_Condition(
        int analogvalue,        String value,        String comparator    ) {
        this.analogvalue = analogvalue;
        this.value = value;
        this.comparator = comparator;
    }


    public int getAnalogvalue() {
        return analogvalue;
    }

    public void setAnalogvalue(int analogvalue) {
        this.analogvalue = analogvalue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getComparator() {
        return comparator;
    }

    public void setComparator(String comparator) {
        this.comparator = comparator;
    }

    public arduinoML_Sensor getArduinoml_sensor() {
        return arduinoml_sensor;
    }

    public void setArduinoml_sensor(arduinoML_Sensor arduinoml_sensor) {
        this.arduinoml_sensor = arduinoml_sensor;
    }

}