





import java.util.List;
import java.util.ArrayList;

public class arduino_ArduinoAnalogModule extends ArduinoModule {






    private arduino_AnalogPin arduino_analogpin;


    public arduino_ArduinoAnalogModule(
    ) {
        super(
        );
    }



    public arduino_AnalogPin getArduino_analogpin() {
        return arduino_analogpin;
    }

    public void setArduino_analogpin(arduino_AnalogPin arduino_analogpin) {
        this.arduino_analogpin = arduino_analogpin;
    }

}