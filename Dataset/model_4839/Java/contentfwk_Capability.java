





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Capability extends Element {

    private String businessValue;
    private String increments;





    private contentfwk_WorkPackage contentfwk_workpackage;




    private contentfwk_WorkPackage contentfwk_workpackage;


    public contentfwk_Capability(
        String businessValue,        String increments    ) {
        super(
        );
        this.businessValue = businessValue;
        this.increments = increments;
    }


    public String getBusinessvalue() {
        return businessValue;
    }

    public void setBusinessvalue(String businessValue) {
        this.businessValue = businessValue;
    }
    public String getIncrements() {
        return increments;
    }

    public void setIncrements(String increments) {
        this.increments = increments;
    }

    public contentfwk_WorkPackage getContentfwk_workpackage() {
        return contentfwk_workpackage;
    }

    public void setContentfwk_workpackage(contentfwk_WorkPackage contentfwk_workpackage) {
        this.contentfwk_workpackage = contentfwk_workpackage;
    }
    public contentfwk_WorkPackage getContentfwk_workpackage() {
        return contentfwk_workpackage;
    }

    public void setContentfwk_workpackage(contentfwk_WorkPackage contentfwk_workpackage) {
        this.contentfwk_workpackage = contentfwk_workpackage;
    }

}