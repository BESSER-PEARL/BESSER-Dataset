





import java.util.List;
import java.util.ArrayList;

public class iotw_I2CLCD extends OutputDevice {

    private String pinVcc;
    private String pinSDA;
    private String pinGND;
    private String pinSCL;
    private String type;



    public iotw_I2CLCD(
        String pinVcc,        String pinSDA,        String pinGND,        String pinSCL,        String type    ) {
        super(
        );
        this.pinVcc = pinVcc;
        this.pinSDA = pinSDA;
        this.pinGND = pinGND;
        this.pinSCL = pinSCL;
        this.type = type;
    }


    public String getPinvcc() {
        return pinVcc;
    }

    public void setPinvcc(String pinVcc) {
        this.pinVcc = pinVcc;
    }
    public String getPinsda() {
        return pinSDA;
    }

    public void setPinsda(String pinSDA) {
        this.pinSDA = pinSDA;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPinscl() {
        return pinSCL;
    }

    public void setPinscl(String pinSCL) {
        this.pinSCL = pinSCL;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}