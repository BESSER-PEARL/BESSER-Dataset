





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Action  {

    private String value;





    private arduinoML_State arduinoml_state;


    public arduinoML_Action(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public arduinoML_State getArduinoml_state() {
        return arduinoml_state;
    }

    public void setArduinoml_state(arduinoML_State arduinoml_state) {
        this.arduinoml_state = arduinoml_state;
    }

}