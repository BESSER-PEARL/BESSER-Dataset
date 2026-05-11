





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Trigger  {

    private String value;





    private List<arduinoml_Sensor> arduinoml_sensors;




    private arduinoml_Transition arduinoml_transition;


    public arduinoml_Trigger(
        String value    ) {
        this.value = value;
        this.arduinoml_sensors = new ArrayList<>();
    }

    public arduinoml_Trigger(
        String value        ArrayList<arduinoml_Sensor> arduinoml_sensors    ) {
        this.value = value;
        this.arduinoml_sensors = arduinoml_sensors;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<arduinoml_Sensor> getArduinoml_sensors() {
        return arduinoml_sensors;
    }

    public void addArduinoml_sensor(Arduinoml_sensor arduinoml_sensor) {
        this.arduinoml_sensors.add(arduinoml_sensor);
    }
    public arduinoml_Transition getArduinoml_transition() {
        return arduinoml_transition;
    }

    public void setArduinoml_transition(arduinoml_Transition arduinoml_transition) {
        this.arduinoml_transition = arduinoml_transition;
    }

}