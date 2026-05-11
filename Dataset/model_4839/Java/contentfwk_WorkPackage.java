





import java.util.List;
import java.util.ArrayList;

public class contentfwk_WorkPackage extends StrategicElement {

    private String workPackageCategory;



    public contentfwk_WorkPackage(
        String workPackageCategory    ) {
        super(
        );
        this.workPackageCategory = workPackageCategory;
    }


    public String getWorkpackagecategory() {
        return workPackageCategory;
    }

    public void setWorkpackagecategory(String workPackageCategory) {
        this.workPackageCategory = workPackageCategory;
    }


}