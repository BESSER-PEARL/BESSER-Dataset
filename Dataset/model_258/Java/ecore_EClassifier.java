





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceClass;
    private String instanceClassName;
    private String defaultValue;



    public ecore_EClassifier(
        String instanceClass,        String instanceClassName,        String defaultValue    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.instanceClassName = instanceClassName;
        this.defaultValue = defaultValue;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}