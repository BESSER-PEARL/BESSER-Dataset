





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Pinref  {

    private String pin;
    private String part;
    private String gate;





    private eaglemodel_Segment eaglemodel_segment;


    public eaglemodel_Pinref(
        String pin,        String part,        String gate    ) {
        this.pin = pin;
        this.part = part;
        this.gate = gate;
    }


    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getPart() {
        return part;
    }

    public void setPart(String part) {
        this.part = part;
    }
    public String getGate() {
        return gate;
    }

    public void setGate(String gate) {
        this.gate = gate;
    }

    public eaglemodel_Segment getEaglemodel_segment() {
        return eaglemodel_segment;
    }

    public void setEaglemodel_segment(eaglemodel_Segment eaglemodel_segment) {
        this.eaglemodel_segment = eaglemodel_segment;
    }

}