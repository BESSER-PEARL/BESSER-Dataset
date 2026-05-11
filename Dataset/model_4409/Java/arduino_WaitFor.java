





import java.util.List;
import java.util.ArrayList;

public class arduino_WaitFor extends Utilities {

    private String mode;





    private arduino_Pin arduino_pin;


    public arduino_WaitFor(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public arduino_Pin getArduino_pin() {
        return arduino_pin;
    }

    public void setArduino_pin(arduino_Pin arduino_pin) {
        this.arduino_pin = arduino_pin;
    }

}