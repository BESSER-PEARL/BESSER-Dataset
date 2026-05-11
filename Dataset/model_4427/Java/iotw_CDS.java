





import java.util.List;
import java.util.ArrayList;

public class iotw_CDS extends InputDevice {

    private String pinVcc;
    private String pinD0;
    private String pinGND;



    public iotw_CDS(
        String pinVcc,        String pinD0,        String pinGND    ) {
        super(
        );
        this.pinVcc = pinVcc;
        this.pinD0 = pinD0;
        this.pinGND = pinGND;
    }


    public String getPinvcc() {
        return pinVcc;
    }

    public void setPinvcc(String pinVcc) {
        this.pinVcc = pinVcc;
    }
    public String getPind0() {
        return pinD0;
    }

    public void setPind0(String pinD0) {
        this.pinD0 = pinD0;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }


}