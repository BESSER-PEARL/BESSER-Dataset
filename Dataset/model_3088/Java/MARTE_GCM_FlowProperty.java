





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_FlowProperty  {

    private String direction;





    private GCM_MARTE_Property gcm_marte_property;


    public MARTE_GCM_FlowProperty(
        String direction    ) {
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public GCM_MARTE_Property getGcm_marte_property() {
        return gcm_marte_property;
    }

    public void setGcm_marte_property(GCM_MARTE_Property gcm_marte_property) {
        this.gcm_marte_property = gcm_marte_property;
    }

}