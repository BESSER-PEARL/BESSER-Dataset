





import java.util.List;
import java.util.ArrayList;

public class arduino_ArduinoBoard extends Board {






    private List<arduino_AnalogPin> arduino_analogpins;




    private List<arduino_DigitalPin> arduino_digitalpins;


    public arduino_ArduinoBoard(
    ) {
        super(
        );
        this.arduino_analogpins = new ArrayList<>();
        this.arduino_digitalpins = new ArrayList<>();
    }

    public arduino_ArduinoBoard(
        ArrayList<arduino_AnalogPin> arduino_analogpins,        ArrayList<arduino_DigitalPin> arduino_digitalpins    ) {
        this.arduino_analogpins = arduino_analogpins;
        this.arduino_digitalpins = arduino_digitalpins;
    }


    public List<arduino_AnalogPin> getArduino_analogpins() {
        return arduino_analogpins;
    }

    public void addArduino_analogpin(Arduino_analogpin arduino_analogpin) {
        this.arduino_analogpins.add(arduino_analogpin);
    }
    public List<arduino_DigitalPin> getArduino_digitalpins() {
        return arduino_digitalpins;
    }

    public void addArduino_digitalpin(Arduino_digitalpin arduino_digitalpin) {
        this.arduino_digitalpins.add(arduino_digitalpin);
    }

}