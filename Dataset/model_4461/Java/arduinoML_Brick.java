





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Brick extends NamedElement {

    private String type;
    private int pin;





    private arduinoML_App arduinoml_app;


    public arduinoML_Brick(
        String type,        int pin    ) {
        super(
        );
        this.type = type;
        this.pin = pin;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }

    public arduinoML_App getArduinoml_app() {
        return arduinoml_app;
    }

    public void setArduinoml_app(arduinoML_App arduinoml_app) {
        this.arduinoml_app = arduinoml_app;
    }

}