





import java.util.List;
import java.util.ArrayList;

public class arduinoml_DigitalAction extends Action {

    private String dState;





    private arduinoml_DigitalActuator arduinoml_digitalactuator;


    public arduinoml_DigitalAction(
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

    public arduinoml_DigitalActuator getArduinoml_digitalactuator() {
        return arduinoml_digitalactuator;
    }

    public void setArduinoml_digitalactuator(arduinoml_DigitalActuator arduinoml_digitalactuator) {
        this.arduinoml_digitalactuator = arduinoml_digitalactuator;
    }

}