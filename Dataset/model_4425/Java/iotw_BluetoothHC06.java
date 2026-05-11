





import java.util.List;
import java.util.ArrayList;

public class iotw_BluetoothHC06 extends ConnectivityControl {

    private String pinRXD;
    private String pinVCC;
    private String pinGND;
    private String pinTXD;



    public iotw_BluetoothHC06(
        String pinRXD,        String pinVCC,        String pinGND,        String pinTXD    ) {
        super(
        );
        this.pinRXD = pinRXD;
        this.pinVCC = pinVCC;
        this.pinGND = pinGND;
        this.pinTXD = pinTXD;
    }


    public String getPinrxd() {
        return pinRXD;
    }

    public void setPinrxd(String pinRXD) {
        this.pinRXD = pinRXD;
    }
    public String getPinvcc() {
        return pinVCC;
    }

    public void setPinvcc(String pinVCC) {
        this.pinVCC = pinVCC;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPintxd() {
        return pinTXD;
    }

    public void setPintxd(String pinTXD) {
        this.pinTXD = pinTXD;
    }


}