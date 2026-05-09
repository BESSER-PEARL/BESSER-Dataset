





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceClassName;
    private String instanceClass;
    private String instanceTypeName;
    private String defaultValue;





    private List<ecore_ETypeParameter> ecore_etypeparameters;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_EPackage ecore_epackage;




    private ecore_ETypedElement ecore_etypedelement;




    private ecore_EPackage ecore_epackage;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_EOperation ecore_eoperation;


    public ecore_EClassifier(
        String instanceClassName,        String instanceClass,        String instanceTypeName,        String defaultValue    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.instanceClass = instanceClass;
        this.instanceTypeName = instanceTypeName;
        this.defaultValue = defaultValue;
        this.ecore_etypeparameters = new ArrayList<>();
    }

    public ecore_EClassifier(
        String instanceClassName,        String instanceClass,        String instanceTypeName,        String defaultValue        ArrayList<ecore_ETypeParameter> ecore_etypeparameters    ) {
        this.instanceClassName = instanceClassName;
        this.instanceClass = instanceClass;
        this.instanceTypeName = instanceTypeName;
        this.defaultValue = defaultValue;
        this.ecore_etypeparameters = ecore_etypeparameters;
    }

    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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
    public ecore_EPackage getEcore_epackage() {
        return ecore_epackage;
    }

    public void setEcore_epackage(ecore_EPackage ecore_epackage) {
        this.ecore_epackage = ecore_epackage;
    }
    public ecore_ETypedElement getEcore_etypedelement() {
        return ecore_etypedelement;
    }

    public void setEcore_etypedelement(ecore_ETypedElement ecore_etypedelement) {
        this.ecore_etypedelement = ecore_etypedelement;
    }
    public ecore_EPackage getEcore_epackage() {
        return ecore_epackage;
    }

    public void setEcore_epackage(ecore_EPackage ecore_epackage) {
        this.ecore_epackage = ecore_epackage;
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