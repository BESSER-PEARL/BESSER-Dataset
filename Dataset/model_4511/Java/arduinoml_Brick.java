





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Brick extends NamedElement {

    private int pin;





    private arduinoml_AMLMachine arduinoml_amlmachine;


    public arduinoml_Brick(
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

    public arduinoml_AMLMachine getArduinoml_amlmachine() {
        return arduinoml_amlmachine;
    }

    public void setArduinoml_amlmachine(arduinoml_AMLMachine arduinoml_amlmachine) {
        this.arduinoml_amlmachine = arduinoml_amlmachine;
    }

}