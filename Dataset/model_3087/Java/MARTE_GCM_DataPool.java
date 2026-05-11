





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_DataPool  {

    private String ordering;





    private GCM_MARTE_Property gcm_marte_property;


    public MARTE_GCM_DataPool(
        String ordering    ) {
        this.ordering = ordering;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public GCM_MARTE_Property getGcm_marte_property() {
        return gcm_marte_property;
    }

    public void setGcm_marte_property(GCM_MARTE_Property gcm_marte_property) {
        this.gcm_marte_property = gcm_marte_property;
    }

}