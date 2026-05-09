





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceClass;
    private String defaultValue;
    private String instanceTypeName;
    private String instanceClassName;



    public ecore_EClassifier(
        String instanceClass,        String defaultValue,        String instanceTypeName,        String instanceClassName    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
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