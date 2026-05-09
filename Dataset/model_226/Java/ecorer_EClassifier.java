





import java.util.List;
import java.util.ArrayList;

public class ecorer_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceTypeName;
    private String instanceClass;
    private String instanceClassName;





    private ecorer_EOperation ecorer_eoperation;


    public ecorer_EClassifier(
        String defaultValue,        String instanceTypeName,        String instanceClass,        String instanceClassName    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceTypeName = instanceTypeName;
        this.instanceClass = instanceClass;
        this.instanceClassName = instanceClassName;
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

    public ecorer_EOperation getEcorer_eoperation() {
        return ecorer_eoperation;
    }

    public void setEcorer_eoperation(ecorer_EOperation ecorer_eoperation) {
        this.ecorer_eoperation = ecorer_eoperation;
    }

}