





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Action extends NamedElement {

    private String value;





    private arduinoml_Actuator arduinoml_actuator;


    public arduinoml_Action(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public arduinoml_Actuator getArduinoml_actuator() {
        return arduinoml_actuator;
    }

    public void setArduinoml_actuator(arduinoml_Actuator arduinoml_actuator) {
        this.arduinoml_actuator = arduinoml_actuator;
    }

}