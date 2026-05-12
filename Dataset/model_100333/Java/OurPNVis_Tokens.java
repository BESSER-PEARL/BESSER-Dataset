





import java.util.List;
import java.util.ArrayList;

public class OurPNVis_Tokens extends Attribute {

    private String text;





    private OurPNVis_Place ourpnvis_place;


    public OurPNVis_Tokens(
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

    public OurPNVis_Place getOurpnvis_place() {
        return ourpnvis_place;
    }

    public void setOurpnvis_place(OurPNVis_Place ourpnvis_place) {
        this.ourpnvis_place = ourpnvis_place;
    }

}