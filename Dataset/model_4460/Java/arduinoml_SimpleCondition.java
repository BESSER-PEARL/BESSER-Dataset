





import java.util.List;
import java.util.ArrayList;

public class arduinoml_SimpleCondition extends Condition {

    private String value;
    private String comparator;





    private arduinoml_Sensor arduinoml_sensor;




    private arduinoml_MultipleCondition arduinoml_multiplecondition;


    public arduinoml_SimpleCondition(
        String value,        String comparator    ) {
        super(
        );
        this.value = value;
        this.comparator = comparator;
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

    public arduinoml_Sensor getArduinoml_sensor() {
        return arduinoml_sensor;
    }

    public void setArduinoml_sensor(arduinoml_Sensor arduinoml_sensor) {
        this.arduinoml_sensor = arduinoml_sensor;
    }
    public arduinoml_MultipleCondition getArduinoml_multiplecondition() {
        return arduinoml_multiplecondition;
    }

    public void setArduinoml_multiplecondition(arduinoml_MultipleCondition arduinoml_multiplecondition) {
        this.arduinoml_multiplecondition = arduinoml_multiplecondition;
    }

}