





import java.util.List;
import java.util.ArrayList;

public class OurPNVis_ident extends Label {

    private String text;





    private OurPNVis_Arc ourpnvis_arc;


    public OurPNVis_ident(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public OurPNVis_Arc getOurpnvis_arc() {
        return ourpnvis_arc;
    }

    public void setOurpnvis_arc(OurPNVis_Arc ourpnvis_arc) {
        this.ourpnvis_arc = ourpnvis_arc;
    }

}