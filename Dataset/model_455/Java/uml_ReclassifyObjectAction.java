





import java.util.List;
import java.util.ArrayList;

public class uml_ReclassifyObjectAction extends Action {

    private String isReplaceAll;





    private List<uml_Classifier> uml_classifiers;




    private List<uml_Classifier> uml_classifiers;


    public uml_ReclassifyObjectAction(
        String isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
        this.uml_classifiers = new ArrayList<>();
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_ReclassifyObjectAction(
        String isReplaceAll        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.isReplaceAll = isReplaceAll;
        this.uml_classifiers = uml_classifiers;
        this.uml_classifiers = uml_classifiers;
    }

    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}