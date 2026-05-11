





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Action  {

    private int analogvalue;
    private String value;





    private arduinoML_Actuator arduinoml_actuator;




    private arduinoML_State arduinoml_state;


    public arduinoML_Action(
        int analogvalue,        String value    ) {
        this.analogvalue = analogvalue;
        this.value = value;
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

    public arduinoML_Actuator getArduinoml_actuator() {
        return arduinoml_actuator;
    }

    public void setArduinoml_actuator(arduinoML_Actuator arduinoml_actuator) {
        this.arduinoml_actuator = arduinoml_actuator;
    }
    public arduinoML_State getArduinoml_state() {
        return arduinoml_state;
    }

    public void setArduinoml_state(arduinoML_State arduinoml_state) {
        this.arduinoml_state = arduinoml_state;
    }

}