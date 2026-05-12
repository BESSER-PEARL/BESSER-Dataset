





import java.util.List;
import java.util.ArrayList;

public class UML2_ReclassifyObjectAction extends Action {

    private boolean isReplaceAll;





    private List<UML2_Classifier> uml2_classifiers;




    private UML2_InputPin uml2_inputpin;




    private List<UML2_Classifier> uml2_classifiers;


    public UML2_ReclassifyObjectAction(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
        this.uml2_classifiers = new ArrayList<>();
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_ReclassifyObjectAction(
        boolean isReplaceAll        ArrayList<UML2_Classifier> uml2_classifiers,        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.isReplaceAll = isReplaceAll;
        this.uml2_classifiers = uml2_classifiers;
        this.uml2_classifiers = uml2_classifiers;
    }

    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }

}