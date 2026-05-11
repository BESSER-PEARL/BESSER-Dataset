





import java.util.List;
import java.util.ArrayList;

public class behaviour_Drone extends NamedElement {

    private String typeName;
    private String travelMode;



    public behaviour_Drone(
        String typeName,        String travelMode    ) {
        super(
        );
        this.typeName = typeName;
        this.travelMode = travelMode;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getTravelmode() {
        return travelMode;
    }

    public void setTravelmode(String travelMode) {
        this.travelMode = travelMode;
    }


}