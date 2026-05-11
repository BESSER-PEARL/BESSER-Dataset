





import java.util.List;
import java.util.ArrayList;

public class contentfwk_WorkPackage extends StrategicElement {

    private String workPackageCategory;
    private String capabilityDelivered;





    private contentfwk_Capability contentfwk_capability;




    private List<contentfwk_Capability> contentfwk_capabilitys;


    public contentfwk_WorkPackage(
        String workPackageCategory,        String capabilityDelivered    ) {
        super(
        );
        this.workPackageCategory = workPackageCategory;
        this.capabilityDelivered = capabilityDelivered;
        this.contentfwk_capabilitys = new ArrayList<>();
    }

    public contentfwk_WorkPackage(
        String workPackageCategory,        String capabilityDelivered        ArrayList<contentfwk_Capability> contentfwk_capabilitys    ) {
        this.workPackageCategory = workPackageCategory;
        this.capabilityDelivered = capabilityDelivered;
        this.contentfwk_capabilitys = contentfwk_capabilitys;
    }

    public String getWorkpackagecategory() {
        return workPackageCategory;
    }

    public void setWorkpackagecategory(String workPackageCategory) {
        this.workPackageCategory = workPackageCategory;
    }
    public String getCapabilitydelivered() {
        return capabilityDelivered;
    }

    public void setCapabilitydelivered(String capabilityDelivered) {
        this.capabilityDelivered = capabilityDelivered;
    }

    public contentfwk_Capability getContentfwk_capability() {
        return contentfwk_capability;
    }

    public void setContentfwk_capability(contentfwk_Capability contentfwk_capability) {
        this.contentfwk_capability = contentfwk_capability;
    }
    public List<contentfwk_Capability> getContentfwk_capabilitys() {
        return contentfwk_capabilitys;
    }

    public void addContentfwk_capability(Contentfwk_capability contentfwk_capability) {
        this.contentfwk_capabilitys.add(contentfwk_capability);
    }

}