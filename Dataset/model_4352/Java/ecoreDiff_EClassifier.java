





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EClassifier extends ENamedElement {

    private String instanceTypeName;
    private String instanceClassName;





    private ecoreDiff_EObject ecorediff_eobject;




    private ecoreDiff_ChangedEClassifier ecorediff_changedeclassifier;


    public ecoreDiff_EClassifier(
        String instanceTypeName,        String instanceClassName    ) {
        super(
        );
        this.instanceTypeName = instanceTypeName;
        this.instanceClassName = instanceClassName;
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

    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }
    public ecoreDiff_ChangedEClassifier getEcorediff_changedeclassifier() {
        return ecorediff_changedeclassifier;
    }

    public void setEcorediff_changedeclassifier(ecoreDiff_ChangedEClassifier ecorediff_changedeclassifier) {
        this.ecorediff_changedeclassifier = ecorediff_changedeclassifier;
    }

}