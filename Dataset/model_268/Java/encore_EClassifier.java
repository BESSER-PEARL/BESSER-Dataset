





import java.util.List;
import java.util.ArrayList;

public class encore_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceClass;
    private String instanceTypeName;
    private String instanceClassName;





    private encore_EGenericType encore_egenerictype;




    private List<encore_ETypeParameter> encore_etypeparameters;




    private encore_EPackage encore_epackage;




    private encore_EGenericType encore_egenerictype;




    private encore_EOperation encore_eoperation;




    private encore_EPackage encore_epackage;


    public encore_EClassifier(
        String defaultValue,        String instanceClass,        String instanceTypeName,        String instanceClassName    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceClass = instanceClass;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
        this.encore_etypeparameters = new ArrayList<>();
    }

    public encore_EClassifier(
        String defaultValue,        String instanceClass,        String instanceTypeName,        String instanceClassName        ArrayList<encore_ETypeParameter> encore_etypeparameters    ) {
        this.defaultValue = defaultValue;
        this.instanceClass = instanceClass;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
        this.encore_etypeparameters = encore_etypeparameters;
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

    public encore_EGenericType getEncore_egenerictype() {
        return encore_egenerictype;
    }

    public void setEncore_egenerictype(encore_EGenericType encore_egenerictype) {
        this.encore_egenerictype = encore_egenerictype;
    }
    public List<encore_ETypeParameter> getEncore_etypeparameters() {
        return encore_etypeparameters;
    }

    public void addEncore_etypeparameter(Encore_etypeparameter encore_etypeparameter) {
        this.encore_etypeparameters.add(encore_etypeparameter);
    }
    public encore_EPackage getEncore_epackage() {
        return encore_epackage;
    }

    public void setEncore_epackage(encore_EPackage encore_epackage) {
        this.encore_epackage = encore_epackage;
    }
    public encore_EGenericType getEncore_egenerictype() {
        return encore_egenerictype;
    }

    public void setEncore_egenerictype(encore_EGenericType encore_egenerictype) {
        this.encore_egenerictype = encore_egenerictype;
    }
    public encore_EOperation getEncore_eoperation() {
        return encore_eoperation;
    }

    public void setEncore_eoperation(encore_EOperation encore_eoperation) {
        this.encore_eoperation = encore_eoperation;
    }
    public encore_EPackage getEncore_epackage() {
        return encore_epackage;
    }

    public void setEncore_epackage(encore_EPackage encore_epackage) {
        this.encore_epackage = encore_epackage;
    }

}