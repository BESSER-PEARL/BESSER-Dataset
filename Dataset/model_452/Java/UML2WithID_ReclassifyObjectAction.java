





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ReclassifyObjectAction extends Action {

    private boolean isReplaceAll;





    private List<UML2WithID_Classifier> uml2withid_classifiers;




    private List<UML2WithID_Classifier> uml2withid_classifiers;


    public UML2WithID_ReclassifyObjectAction(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
        this.uml2withid_classifiers = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_ReclassifyObjectAction(
        boolean isReplaceAll        ArrayList<UML2WithID_Classifier> uml2withid_classifiers,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.isReplaceAll = isReplaceAll;
        this.uml2withid_classifiers = uml2withid_classifiers;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }

    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }

}