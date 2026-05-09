





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceTypeName;
    private String instanceClassName;
    private String instanceClass;





    private EPackage epackage;




    private List<ETypeParameter> etypeparameters;


    public ecore_EClassifier(
        String defaultValue,        String instanceTypeName,        String instanceClassName,        String instanceClass    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
        this.instanceClass = instanceClass;
        this.etypeparameters = new ArrayList<>();
    }

    public ecore_EClassifier(
        String defaultValue,        String instanceTypeName,        String instanceClassName,        String instanceClass        ArrayList<ETypeParameter> etypeparameters    ) {
        this.defaultValue = defaultValue;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
        this.instanceClass = instanceClass;
        this.etypeparameters = etypeparameters;
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
    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }

    public EPackage getEpackage() {
        return epackage;
    }

    public void setEpackage(EPackage epackage) {
        this.epackage = epackage;
    }
    public List<ETypeParameter> getEtypeparameters() {
        return etypeparameters;
    }

    public void addEtypeparameter(Etypeparameter etypeparameter) {
        this.etypeparameters.add(etypeparameter);
    }

}