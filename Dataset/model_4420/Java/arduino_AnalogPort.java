





import java.util.List;
import java.util.ArrayList;

public class arduino_AnalogPort extends Port {

    private float value;





    private arduino_Arduino arduino_arduino;


    public arduino_AnalogPort(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public arduino_Arduino getArduino_arduino() {
        return arduino_arduino;
    }

    public void setArduino_arduino(arduino_Arduino arduino_arduino) {
        this.arduino_arduino = arduino_arduino;
    }

}