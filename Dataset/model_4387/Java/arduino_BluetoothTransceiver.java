





import java.util.List;
import java.util.ArrayList;

public class arduino_BluetoothTransceiver extends ArduinoAnalogModule {

    private String dataReceived;
    private String dataToSend;





    private List<arduino_BluetoothTransceiver> arduino_bluetoothtransceivers;


    public arduino_BluetoothTransceiver(
        String dataReceived,        String dataToSend    ) {
        super(
        );
        this.dataReceived = dataReceived;
        this.dataToSend = dataToSend;
        this.arduino_bluetoothtransceivers = new ArrayList<>();
    }

    public arduino_BluetoothTransceiver(
        String dataReceived,        String dataToSend        ArrayList<arduino_BluetoothTransceiver> arduino_bluetoothtransceivers    ) {
        this.dataReceived = dataReceived;
        this.dataToSend = dataToSend;
        this.arduino_bluetoothtransceivers = arduino_bluetoothtransceivers;
    }

    public String getDatareceived() {
        return dataReceived;
    }

    public void setDatareceived(String dataReceived) {
        this.dataReceived = dataReceived;
    }
    public String getDatatosend() {
        return dataToSend;
    }

    public void setDatatosend(String dataToSend) {
        this.dataToSend = dataToSend;
    }

    public List<arduino_BluetoothTransceiver> getArduino_bluetoothtransceivers() {
        return arduino_bluetoothtransceivers;
    }

    public void addArduino_bluetoothtransceiver(Arduino_bluetoothtransceiver arduino_bluetoothtransceiver) {
        this.arduino_bluetoothtransceivers.add(arduino_bluetoothtransceiver);
    }

}