





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EClassifier extends ENamedElement {

    private String instanceTypeName;
    private String instanceClass;
    private String instanceClassName;



    public RefinementsEcore_EClassifier(
        String instanceTypeName,        String instanceClass,        String instanceClassName    ) {
        super(
        );
        this.instanceTypeName = instanceTypeName;
        this.instanceClass = instanceClass;
        this.instanceClassName = instanceClassName;
    }


    public String getInstancetypename() {
        return instanceTypeName;
    }

    public void setInstancetypename(String instanceTypeName) {
        this.instanceTypeName = instanceTypeName;
    }
    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }


}