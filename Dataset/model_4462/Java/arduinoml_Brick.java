





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Brick extends NamedElement {

    private String pin;





    private arduinoml_App arduinoml_app;


    public arduinoml_Brick(
        String pin    ) {
        super(
        );
        this.pin = pin;
    }


    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }

    public arduinoml_App getArduinoml_app() {
        return arduinoml_app;
    }

    public void setArduinoml_app(arduinoml_App arduinoml_app) {
        this.arduinoml_app = arduinoml_app;
    }

}