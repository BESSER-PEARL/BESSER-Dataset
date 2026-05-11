





import java.util.List;
import java.util.ArrayList;

public class contentfwk_WorkPackage extends StrategicElement {

    private String workPackageCategory;





    private List<contentfwk_Capability> contentfwk_capabilitys;




    private contentfwk_Capability contentfwk_capability;


    public contentfwk_WorkPackage(
        String workPackageCategory    ) {
        super(
        );
        this.workPackageCategory = workPackageCategory;
        this.contentfwk_capabilitys = new ArrayList<>();
    }

    public contentfwk_WorkPackage(
        String workPackageCategory        ArrayList<contentfwk_Capability> contentfwk_capabilitys    ) {
        this.workPackageCategory = workPackageCategory;
        this.contentfwk_capabilitys = contentfwk_capabilitys;
    }

    public String getWorkpackagecategory() {
        return workPackageCategory;
    }

    public void setWorkpackagecategory(String workPackageCategory) {
        this.workPackageCategory = workPackageCategory;
    }

    public List<contentfwk_Capability> getContentfwk_capabilitys() {
        return contentfwk_capabilitys;
    }

    public void addContentfwk_capability(Contentfwk_capability contentfwk_capability) {
        this.contentfwk_capabilitys.add(contentfwk_capability);
    }
    public contentfwk_Capability getContentfwk_capability() {
        return contentfwk_capability;
    }

    public void setContentfwk_capability(contentfwk_Capability contentfwk_capability) {
        this.contentfwk_capability = contentfwk_capability;
    }

}