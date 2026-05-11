





import java.util.List;
import java.util.ArrayList;

public class arduinoml_ActuatorState  {

    private boolean isOn;





    private arduinoml_Actuator arduinoml_actuator;




    private arduinoml_Transition arduinoml_transition;


    public arduinoml_ActuatorState(
        boolean isOn    ) {
        this.isOn = isOn;
    }


    public boolean getIson() {
        return isOn;
    }

    public void setIson(boolean isOn) {
        this.isOn = isOn;
    }

    public arduinoml_Actuator getArduinoml_actuator() {
        return arduinoml_actuator;
    }

    public void setArduinoml_actuator(arduinoml_Actuator arduinoml_actuator) {
        this.arduinoml_actuator = arduinoml_actuator;
    }
    public arduinoml_Transition getArduinoml_transition() {
        return arduinoml_transition;
    }

    public void setArduinoml_transition(arduinoml_Transition arduinoml_transition) {
        this.arduinoml_transition = arduinoml_transition;
    }

}