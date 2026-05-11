





import java.util.List;
import java.util.ArrayList;

public class iotw_BluetoothHC06 extends Connectivity {

    private String pinTXD;
    private String pinVCC;
    private String pinGND;
    private String pinRXD;



    public iotw_BluetoothHC06(
        String pinTXD,        String pinVCC,        String pinGND,        String pinRXD    ) {
        super(
        );
        this.pinTXD = pinTXD;
        this.pinVCC = pinVCC;
        this.pinGND = pinGND;
        this.pinRXD = pinRXD;
    }


    public String getPintxd() {
        return pinTXD;
    }

    public void setPintxd(String pinTXD) {
        this.pinTXD = pinTXD;
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
    public String getPinrxd() {
        return pinRXD;
    }

    public void setPinrxd(String pinRXD) {
        this.pinRXD = pinRXD;
    }


}