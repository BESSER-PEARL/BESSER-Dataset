





import java.util.List;
import java.util.ArrayList;

public class arduinoml_AnalogCondition extends Condition {

    private String aComp;
    private int value;





    private arduinoml_AnalogSensor arduinoml_analogsensor;


    public arduinoml_AnalogCondition(
        String aComp,        int value    ) {
        super(
        );
        this.aComp = aComp;
        this.value = value;
    }


    public String getAcomp() {
        return aComp;
    }

    public void setAcomp(String aComp) {
        this.aComp = aComp;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public arduinoml_AnalogSensor getArduinoml_analogsensor() {
        return arduinoml_analogsensor;
    }

    public void setArduinoml_analogsensor(arduinoml_AnalogSensor arduinoml_analogsensor) {
        this.arduinoml_analogsensor = arduinoml_analogsensor;
    }

}