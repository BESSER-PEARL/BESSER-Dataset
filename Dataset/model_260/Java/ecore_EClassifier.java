





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceClass;
    private String defaultValue;
    private String instanceClassName;





    private ecore_EOperation ecore_eoperation;




    private ecore_ETypedElement ecore_etypedelement;


    public ecore_EClassifier(
        String instanceClass,        String defaultValue,        String instanceClassName    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
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
    public ecore_ETypedElement getEcore_etypedelement() {
        return ecore_etypedelement;
    }

    public void setEcore_etypedelement(ecore_ETypedElement ecore_etypedelement) {
        this.ecore_etypedelement = ecore_etypedelement;
    }

}