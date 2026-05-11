





import java.util.List;
import java.util.ArrayList;

public class arduinoml_DigitalCondition extends Condition {

    private String dState;





    private arduinoml_DigitalSensor arduinoml_digitalsensor;


    public arduinoml_DigitalCondition(
        String dState    ) {
        super(
        );
        this.dState = dState;
    }


    public String getDstate() {
        return dState;
    }

    public void setDstate(String dState) {
        this.dState = dState;
    }

    public arduinoml_DigitalSensor getArduinoml_digitalsensor() {
        return arduinoml_digitalsensor;
    }

    public void setArduinoml_digitalsensor(arduinoml_DigitalSensor arduinoml_digitalsensor) {
        this.arduinoml_digitalsensor = arduinoml_digitalsensor;
    }

}