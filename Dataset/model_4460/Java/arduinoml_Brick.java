





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Brick extends NamedElement {

    private int pin;
    private String type;





    private arduinoml_App arduinoml_app;


    public arduinoml_Brick(
        int pin,        String type    ) {
        super(
        );
        this.pin = pin;
        this.type = type;
    }


    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public arduinoml_App getArduinoml_app() {
        return arduinoml_app;
    }

    public void setArduinoml_app(arduinoml_App arduinoml_app) {
        this.arduinoml_app = arduinoml_app;
    }

}