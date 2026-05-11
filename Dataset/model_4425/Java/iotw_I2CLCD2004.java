





import java.util.List;
import java.util.ArrayList;

public class iotw_I2CLCD2004 extends OutputControl {

    private String pinSCL;
    private String pinSDA;
    private String pinVcc;
    private String pinGND;



    public iotw_I2CLCD2004(
        String pinSCL,        String pinSDA,        String pinVcc,        String pinGND    ) {
        super(
        );
        this.pinSCL = pinSCL;
        this.pinSDA = pinSDA;
        this.pinVcc = pinVcc;
        this.pinGND = pinGND;
    }


    public String getPinscl() {
        return pinSCL;
    }

    public void setPinscl(String pinSCL) {
        this.pinSCL = pinSCL;
    }
    public String getPinsda() {
        return pinSDA;
    }

    public void setPinsda(String pinSDA) {
        this.pinSDA = pinSDA;
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


}