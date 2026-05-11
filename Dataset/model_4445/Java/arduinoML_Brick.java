





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Brick extends NamedElement {

    private int pin;





    private arduinoML_Mode arduinoml_mode;




    private arduinoML_App arduinoml_app;


    public arduinoML_Brick(
        int pin    ) {
        super(
        );
        this.pin = pin;
    }


    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }

    public arduinoML_Mode getArduinoml_mode() {
        return arduinoml_mode;
    }

    public void setArduinoml_mode(arduinoML_Mode arduinoml_mode) {
        this.arduinoml_mode = arduinoml_mode;
    }
    public arduinoML_App getArduinoml_app() {
        return arduinoml_app;
    }

    public void setArduinoml_app(arduinoML_App arduinoml_app) {
        this.arduinoml_app = arduinoml_app;
    }

}