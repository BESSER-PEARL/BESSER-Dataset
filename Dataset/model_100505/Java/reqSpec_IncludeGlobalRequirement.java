





import java.util.List;
import java.util.ArrayList;

public class reqSpec_IncludeGlobalRequirement  {

    private String componentCategory;
    private boolean self;





    private reqSpec_EObject reqspec_eobject;


    public reqSpec_IncludeGlobalRequirement(
        String componentCategory,        boolean self    ) {
        this.componentCategory = componentCategory;
        this.self = self;
    }


    public String getComponentcategory() {
        return componentCategory;
    }

    public void setComponentcategory(String componentCategory) {
        this.componentCategory = componentCategory;
    }
    public boolean getSelf() {
        return self;
    }

    public void setSelf(boolean self) {
        this.self = self;
    }

    public reqSpec_EObject getReqspec_eobject() {
        return reqspec_eobject;
    }

    public void setReqspec_eobject(reqSpec_EObject reqspec_eobject) {
        this.reqspec_eobject = reqspec_eobject;
    }

}