





import java.util.List;
import java.util.ArrayList;

public class arduino_DigitalPin extends Pin {






    private arduino_ArduinoDigitalModule arduino_arduinodigitalmodule;




    private arduino_ArduinoBoard arduino_arduinoboard;


    public arduino_DigitalPin(
    ) {
        super(
        );
    }



    public arduino_ArduinoDigitalModule getArduino_arduinodigitalmodule() {
        return arduino_arduinodigitalmodule;
    }

    public void setArduino_arduinodigitalmodule(arduino_ArduinoDigitalModule arduino_arduinodigitalmodule) {
        this.arduino_arduinodigitalmodule = arduino_arduinodigitalmodule;
    }
    public arduino_ArduinoBoard getArduino_arduinoboard() {
        return arduino_arduinoboard;
    }

    public void setArduino_arduinoboard(arduino_ArduinoBoard arduino_arduinoboard) {
        this.arduino_arduinoboard = arduino_arduinoboard;
    }

}