





import java.util.List;
import java.util.ArrayList;

public class sipme_EnterpriseResource extends EnterpriseObject {

    private String resourceOrigin;





    private List<sipme_Capability> sipme_capabilitys;


    public sipme_EnterpriseResource(
        String resourceOrigin    ) {
        super(
        );
        this.resourceOrigin = resourceOrigin;
        this.sipme_capabilitys = new ArrayList<>();
    }

    public sipme_EnterpriseResource(
        String resourceOrigin        ArrayList<sipme_Capability> sipme_capabilitys    ) {
        this.resourceOrigin = resourceOrigin;
        this.sipme_capabilitys = sipme_capabilitys;
    }

    public String getResourceorigin() {
        return resourceOrigin;
    }

    public void setResourceorigin(String resourceOrigin) {
        this.resourceOrigin = resourceOrigin;
    }

    public List<sipme_Capability> getSipme_capabilitys() {
        return sipme_capabilitys;
    }

    public void addSipme_capability(Sipme_capability sipme_capability) {
        this.sipme_capabilitys.add(sipme_capability);
    }

}