





import java.util.List;
import java.util.ArrayList;

public class ddsm_Resource  {

    private String resourceId;





    private ddsm_CloudElement ddsm_cloudelement;


    public ddsm_Resource(
        String resourceId    ) {
        this.resourceId = resourceId;
    }


    public String getResourceid() {
        return resourceId;
    }

    public void setResourceid(String resourceId) {
        this.resourceId = resourceId;
    }

    public ddsm_CloudElement getDdsm_cloudelement() {
        return ddsm_cloudelement;
    }

    public void setDdsm_cloudelement(ddsm_CloudElement ddsm_cloudelement) {
        this.ddsm_cloudelement = ddsm_cloudelement;
    }

}