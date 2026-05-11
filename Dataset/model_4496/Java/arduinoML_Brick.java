





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Brick extends NamedElement {

    private int pin;



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


}