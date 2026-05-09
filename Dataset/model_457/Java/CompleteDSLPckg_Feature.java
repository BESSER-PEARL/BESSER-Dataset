





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Feature extends RedefinableElement {

    private boolean isStatic;





    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;




    private CompleteDSLPckg_Classifier completedslpckg_classifier;


    public CompleteDSLPckg_Feature(
        boolean isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.completedslpckg_classifiers = new ArrayList<>();
    }

    public CompleteDSLPckg_Feature(
        boolean isStatic        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers    ) {
        this.isStatic = isStatic;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
    }

    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }
    public CompleteDSLPckg_Classifier getCompletedslpckg_classifier() {
        return completedslpckg_classifier;
    }

    public void setCompletedslpckg_classifier(CompleteDSLPckg_Classifier completedslpckg_classifier) {
        this.completedslpckg_classifier = completedslpckg_classifier;
    }

}