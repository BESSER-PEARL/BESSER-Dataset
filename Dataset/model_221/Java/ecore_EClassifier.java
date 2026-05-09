





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceTypeName;
    private String instanceClassName;
    private String defaultValue;
    private String instanceClass;





    private ecore_EOperation ecore_eoperation;


    public ecore_EClassifier(
        String instanceTypeName,        String instanceClassName,        String defaultValue,        String instanceClass    ) {
        super(
        );
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
        this.defaultValue = defaultValue;
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

    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }

}