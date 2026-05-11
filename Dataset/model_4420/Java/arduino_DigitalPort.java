





import java.util.List;
import java.util.ArrayList;

public class arduino_DigitalPort extends Port {

    private int value;





    private arduino_Arduino arduino_arduino;


    public arduino_DigitalPort(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public arduino_Arduino getArduino_arduino() {
        return arduino_arduino;
    }

    public void setArduino_arduino(arduino_Arduino arduino_arduino) {
        this.arduino_arduino = arduino_arduino;
    }

}