





import java.util.List;
import java.util.ArrayList;

public class OurPNVis_KeepAnim extends Attribute {

    private boolean text;





    private OurPNVis_Arc ourpnvis_arc;


    public OurPNVis_KeepAnim(
        boolean text    ) {
        super(
        );
        this.text = text;
    }


    public boolean getText() {
        return text;
    }

    public void setText(boolean text) {
        this.text = text;
    }

    public OurPNVis_Arc getOurpnvis_arc() {
        return ourpnvis_arc;
    }

    public void setOurpnvis_arc(OurPNVis_Arc ourpnvis_arc) {
        this.ourpnvis_arc = ourpnvis_arc;
    }

}