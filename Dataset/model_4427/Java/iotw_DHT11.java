





import java.util.List;
import java.util.ArrayList;

public class iotw_DHT11 extends InputDevice {

    private String pinVcc;
    private String pinGND;
    private String pinData;



    public iotw_DHT11(
        String pinVcc,        String pinGND,        String pinData    ) {
        super(
        );
        this.pinVcc = pinVcc;
        this.pinGND = pinGND;
        this.pinData = pinData;
    }


    public String getPinvcc() {
        return pinVcc;
    }

    public void setPinvcc(String pinVcc) {
        this.pinVcc = pinVcc;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPindata() {
        return pinData;
    }

    public void setPindata(String pinData) {
        this.pinData = pinData;
    }


}