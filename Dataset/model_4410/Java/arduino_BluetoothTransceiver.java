





import java.util.List;
import java.util.ArrayList;

public class arduino_BluetoothTransceiver extends ArduinoAnalogModule {






    private List<arduino_BluetoothTransceiver> arduino_bluetoothtransceivers;


    public arduino_BluetoothTransceiver(
    ) {
        super(
        );
        this.arduino_bluetoothtransceivers = new ArrayList<>();
    }

    public arduino_BluetoothTransceiver(
        ArrayList<arduino_BluetoothTransceiver> arduino_bluetoothtransceivers    ) {
        this.arduino_bluetoothtransceivers = arduino_bluetoothtransceivers;
    }


    public List<arduino_BluetoothTransceiver> getArduino_bluetoothtransceivers() {
        return arduino_bluetoothtransceivers;
    }

    public void addArduino_bluetoothtransceiver(Arduino_bluetoothtransceiver arduino_bluetoothtransceiver) {
        this.arduino_bluetoothtransceivers.add(arduino_bluetoothtransceiver);
    }

}