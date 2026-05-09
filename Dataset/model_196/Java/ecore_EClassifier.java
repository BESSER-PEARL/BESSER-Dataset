





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceClass;
    private String instanceTypeName;
    private String instanceClassName;



    public ecore_EClassifier(
        String defaultValue,        String instanceClass,        String instanceTypeName,        String instanceClassName    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceClass = instanceClass;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public String getInstancetypename() {
        return instanceTypeName;
    }

    public void setInstancetypename(String instanceTypeName) {
        this.instanceTypeName = instanceTypeName;
    }
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }


}