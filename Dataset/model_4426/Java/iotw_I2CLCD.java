





import java.util.List;
import java.util.ArrayList;

public class iotw_I2CLCD extends OutputDevice {

    private String pinVcc;
    private String type;
    private String pinSCL;
    private String pinGND;
    private String pinSDA;



    public iotw_I2CLCD(
        String pinVcc,        String type,        String pinSCL,        String pinGND,        String pinSDA    ) {
        super(
        );
        this.pinVcc = pinVcc;
        this.type = type;
        this.pinSCL = pinSCL;
        this.pinGND = pinGND;
        this.pinSDA = pinSDA;
    }


    public String getPinvcc() {
        return pinVcc;
    }

    public void setPinvcc(String pinVcc) {
        this.pinVcc = pinVcc;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPinscl() {
        return pinSCL;
    }

    public void setPinscl(String pinSCL) {
        this.pinSCL = pinSCL;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPinsda() {
        return pinSDA;
    }

    public void setPinsda(String pinSDA) {
        this.pinSDA = pinSDA;
    }


}