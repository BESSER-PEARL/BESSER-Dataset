





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassifier extends ENamedElement {

    private String instanceClass;
    private int classifierID;
    private String defaultValue;





    private ecore_EOperation ecore_eoperation;


    public ecore_EClassifier(
        String instanceClass,        int classifierID,        String defaultValue    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.classifierID = classifierID;
        this.defaultValue = defaultValue;
    }


    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public int getClassifierid() {
        return classifierID;
    }

    public void setClassifierid(int classifierID) {
        this.classifierID = classifierID;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }

}