





import java.util.List;
import java.util.ArrayList;

public class arduino_BluetoothTransceiver extends ArduinoCommunicationModule {

    private String dataToSend;
    private String dataReceived;





    private List<arduino_BluetoothTransceiver> arduino_bluetoothtransceivers;


    public arduino_BluetoothTransceiver(
        String dataToSend,        String dataReceived    ) {
        super(
        );
        this.dataToSend = dataToSend;
        this.dataReceived = dataReceived;
        this.arduino_bluetoothtransceivers = new ArrayList<>();
    }

    public arduino_BluetoothTransceiver(
        String dataToSend,        String dataReceived        ArrayList<arduino_BluetoothTransceiver> arduino_bluetoothtransceivers    ) {
        this.dataToSend = dataToSend;
        this.dataReceived = dataReceived;
        this.arduino_bluetoothtransceivers = arduino_bluetoothtransceivers;
    }

    public String getDatatosend() {
        return dataToSend;
    }

    public void setDatatosend(String dataToSend) {
        this.dataToSend = dataToSend;
    }
    public String getDatareceived() {
        return dataReceived;
    }

    public void setDatareceived(String dataReceived) {
        this.dataReceived = dataReceived;
    }

    public List<arduino_BluetoothTransceiver> getArduino_bluetoothtransceivers() {
        return arduino_bluetoothtransceivers;
    }

    public void addArduino_bluetoothtransceiver(Arduino_bluetoothtransceiver arduino_bluetoothtransceiver) {
        this.arduino_bluetoothtransceivers.add(arduino_bluetoothtransceiver);
    }

}