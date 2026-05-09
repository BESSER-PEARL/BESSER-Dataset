





import java.util.List;
import java.util.ArrayList;

public class Ecore_EClassifier extends ENamedElement {

    private String instanceClassName;
    private String instanceTypeName;
    private String instanceClass;
    private String defaultValue;



    public Ecore_EClassifier(
        String instanceClassName,        String instanceTypeName,        String instanceClass,        String defaultValue    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.instanceTypeName = instanceTypeName;
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}