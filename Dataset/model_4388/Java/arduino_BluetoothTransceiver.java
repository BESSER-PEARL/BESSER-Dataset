





import java.util.List;
import java.util.ArrayList;

public class arduino_BluetoothTransceiver extends ArduinoAnalogModule {

    private String dataReceived;
    private String dataToSend;





    private arduino_BluetoothTransceiver arduino_bluetoothtransceiver;


    public arduino_BluetoothTransceiver(
        String dataReceived,        String dataToSend    ) {
        super(
        );
        this.dataReceived = dataReceived;
        this.dataToSend = dataToSend;
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

    public arduino_BluetoothTransceiver getArduino_bluetoothtransceiver() {
        return arduino_bluetoothtransceiver;
    }

    public void setArduino_bluetoothtransceiver(arduino_BluetoothTransceiver arduino_bluetoothtransceiver) {
        this.arduino_bluetoothtransceiver = arduino_bluetoothtransceiver;
    }

}