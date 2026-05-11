





import java.util.List;
import java.util.ArrayList;

public class arduino_AnalogPin extends Pin {






    private arduino_ArduinoAnalogModule arduino_arduinoanalogmodule;




    private arduino_ArduinoBoard arduino_arduinoboard;


    public arduino_AnalogPin(
    ) {
        super(
        );
    }



    public arduino_ArduinoAnalogModule getArduino_arduinoanalogmodule() {
        return arduino_arduinoanalogmodule;
    }

    public void setArduino_arduinoanalogmodule(arduino_ArduinoAnalogModule arduino_arduinoanalogmodule) {
        this.arduino_arduinoanalogmodule = arduino_arduinoanalogmodule;
    }
    public arduino_ArduinoBoard getArduino_arduinoboard() {
        return arduino_arduinoboard;
    }

    public void setArduino_arduinoboard(arduino_ArduinoBoard arduino_arduinoboard) {
        this.arduino_arduinoboard = arduino_arduinoboard;
    }

}