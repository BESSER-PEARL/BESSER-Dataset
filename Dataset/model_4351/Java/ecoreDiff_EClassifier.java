





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EClassifier extends ENamedElement {

    private String defaultValue;
    private String instanceTypeName;
    private String instanceClassName;
    private String instanceClass;





    private ecoreDiff_EOperation ecorediff_eoperation;




    private ecoreDiff_ChangedEClassifier ecorediff_changedeclassifier;




    private ecoreDiff_EGenericType ecorediff_egenerictype;




    private ecoreDiff_EGenericType ecorediff_egenerictype;


    public ecoreDiff_EClassifier(
        String defaultValue,        String instanceTypeName,        String instanceClassName,        String instanceClass    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
        this.instanceClass = instanceClass;
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

    public ecoreDiff_EOperation getEcorediff_eoperation() {
        return ecorediff_eoperation;
    }

    public void setEcorediff_eoperation(ecoreDiff_EOperation ecorediff_eoperation) {
        this.ecorediff_eoperation = ecorediff_eoperation;
    }
    public ecoreDiff_ChangedEClassifier getEcorediff_changedeclassifier() {
        return ecorediff_changedeclassifier;
    }

    public void setEcorediff_changedeclassifier(ecoreDiff_ChangedEClassifier ecorediff_changedeclassifier) {
        this.ecorediff_changedeclassifier = ecorediff_changedeclassifier;
    }
    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }
    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }

}