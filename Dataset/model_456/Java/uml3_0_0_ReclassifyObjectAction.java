





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ReclassifyObjectAction extends Action {

    private String isReplaceAll;





    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;


    public uml3_0_0_ReclassifyObjectAction(
        String isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
        this.uml3_0_0_classifiers = new ArrayList<>();
        this.uml3_0_0_classifiers = new ArrayList<>();
    }

    public uml3_0_0_ReclassifyObjectAction(
        String isReplaceAll        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers,        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers    ) {
        this.isReplaceAll = isReplaceAll;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
    }

    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }

}