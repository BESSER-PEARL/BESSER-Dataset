





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceClass;
    private String defaultValue;
    private String instanceClassName;
    private String instanceTypeName;





    private ecore_EGenericType ecore_egenerictype;




    private List<ecore_ETypeParameter> ecore_etypeparameters;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_EOperation ecore_eoperation;


    public ecore_EClassifier(
        String instanceClass,        String defaultValue,        String instanceClassName,        String instanceTypeName    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
        this.instanceClassName = instanceClassName;
        this.instanceTypeName = instanceTypeName;
        this.ecore_etypeparameters = new ArrayList<>();
    }

    public ecore_EClassifier(
        String instanceClass,        String defaultValue,        String instanceClassName,        String instanceTypeName        ArrayList<ecore_ETypeParameter> ecore_etypeparameters    ) {
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
        this.instanceClassName = instanceClassName;
        this.instanceTypeName = instanceTypeName;
        this.ecore_etypeparameters = ecore_etypeparameters;
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

    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public List<ecore_ETypeParameter> getEcore_etypeparameters() {
        return ecore_etypeparameters;
    }

    public void addEcore_etypeparameter(Ecore_etypeparameter ecore_etypeparameter) {
        this.ecore_etypeparameters.add(ecore_etypeparameter);
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }

}