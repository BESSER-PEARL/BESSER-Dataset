





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ReclassifyObjectAction extends Action {

    private boolean isReplaceAll;





    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;




    private CompleteDSLPckg_InputPin completedslpckg_inputpin;




    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;


    public CompleteDSLPckg_ReclassifyObjectAction(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
        this.completedslpckg_classifiers = new ArrayList<>();
        this.completedslpckg_classifiers = new ArrayList<>();
    }

    public CompleteDSLPckg_ReclassifyObjectAction(
        boolean isReplaceAll        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers,        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers    ) {
        this.isReplaceAll = isReplaceAll;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
    }

    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }
    public CompleteDSLPckg_InputPin getCompletedslpckg_inputpin() {
        return completedslpckg_inputpin;
    }

    public void setCompletedslpckg_inputpin(CompleteDSLPckg_InputPin completedslpckg_inputpin) {
        this.completedslpckg_inputpin = completedslpckg_inputpin;
    }
    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }

}