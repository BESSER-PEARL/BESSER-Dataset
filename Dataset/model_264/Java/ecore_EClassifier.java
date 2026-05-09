





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceClass;
    private String instanceClassName;





    private ecore_EOperation ecore_eoperation;


    public ecore_EClassifier(
        String defaultValue,        String instanceClass,        String instanceClassName    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceClass = instanceClass;
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
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }

}