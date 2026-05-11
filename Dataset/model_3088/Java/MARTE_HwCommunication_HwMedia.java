





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwCommunication_HwMedia extends HwCommunication_HwCommunicationResource, GRM_CommunicationMedia {

    private String bandWidth;



    public MARTE_HwCommunication_HwMedia(
        String bandWidth    ) {
        super(
        );
        this.bandWidth = bandWidth;
    }


    public String getBandwidth() {
        return bandWidth;
    }

    public void setBandwidth(String bandWidth) {
        this.bandWidth = bandWidth;
    }


}