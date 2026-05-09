





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceClass;
    private String instanceClassName;
    private String instanceTypeName;





    private ecoreO_EGenericType ecoreo_egenerictype;




    private ecoreO_EGenericType ecoreo_egenerictype;


    public ecoreO_EClassifier(
        String defaultValue,        String instanceClass,        String instanceClassName,        String instanceTypeName    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceClass = instanceClass;
        this.instanceClassName = instanceClassName;
        this.instanceTypeName = instanceTypeName;
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
    public String getInstancetypename() {
        return instanceTypeName;
    }

    public void setInstancetypename(String instanceTypeName) {
        this.instanceTypeName = instanceTypeName;
    }

    public ecoreO_EGenericType getEcoreo_egenerictype() {
        return ecoreo_egenerictype;
    }

    public void setEcoreo_egenerictype(ecoreO_EGenericType ecoreo_egenerictype) {
        this.ecoreo_egenerictype = ecoreo_egenerictype;
    }
    public ecoreO_EGenericType getEcoreo_egenerictype() {
        return ecoreo_egenerictype;
    }

    public void setEcoreo_egenerictype(ecoreO_EGenericType ecoreo_egenerictype) {
        this.ecoreo_egenerictype = ecoreo_egenerictype;
    }

}