





import java.util.List;
import java.util.ArrayList;

public class OurPNVis_CanChange extends Attribute {

    private boolean text;





    private OurPNVis_Place ourpnvis_place;


    public OurPNVis_CanChange(
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

    public OurPNVis_Place getOurpnvis_place() {
        return ourpnvis_place;
    }

    public void setOurpnvis_place(OurPNVis_Place ourpnvis_place) {
        this.ourpnvis_place = ourpnvis_place;
    }

}