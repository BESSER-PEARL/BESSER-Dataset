





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_GeneralizationSet extends PackageableElement {

    private boolean isDisjoint;
    private boolean isCovering;





    private List<CompleteDSLPckg_Generalization> completedslpckg_generalizations;




    private CompleteDSLPckg_Classifier completedslpckg_classifier;




    private CompleteDSLPckg_Generalization completedslpckg_generalization;




    private CompleteDSLPckg_Classifier completedslpckg_classifier;


    public CompleteDSLPckg_GeneralizationSet(
        boolean isDisjoint,        boolean isCovering    ) {
        super(
        );
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
        this.completedslpckg_generalizations = new ArrayList<>();
    }

    public CompleteDSLPckg_GeneralizationSet(
        boolean isDisjoint,        boolean isCovering        ArrayList<CompleteDSLPckg_Generalization> completedslpckg_generalizations    ) {
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
        this.completedslpckg_generalizations = completedslpckg_generalizations;
    }

    public boolean getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(boolean isDisjoint) {
        this.isDisjoint = isDisjoint;
    }
    public boolean getIscovering() {
        return isCovering;
    }

    public void setIscovering(boolean isCovering) {
        this.isCovering = isCovering;
    }

    public List<CompleteDSLPckg_Generalization> getCompletedslpckg_generalizations() {
        return completedslpckg_generalizations;
    }

    public void addCompletedslpckg_generalization(Completedslpckg_generalization completedslpckg_generalization) {
        this.completedslpckg_generalizations.add(completedslpckg_generalization);
    }
    public CompleteDSLPckg_Classifier getCompletedslpckg_classifier() {
        return completedslpckg_classifier;
    }

    public void setCompletedslpckg_classifier(CompleteDSLPckg_Classifier completedslpckg_classifier) {
        this.completedslpckg_classifier = completedslpckg_classifier;
    }
    public CompleteDSLPckg_Generalization getCompletedslpckg_generalization() {
        return completedslpckg_generalization;
    }

    public void setCompletedslpckg_generalization(CompleteDSLPckg_Generalization completedslpckg_generalization) {
        this.completedslpckg_generalization = completedslpckg_generalization;
    }
    public CompleteDSLPckg_Classifier getCompletedslpckg_classifier() {
        return completedslpckg_classifier;
    }

    public void setCompletedslpckg_classifier(CompleteDSLPckg_Classifier completedslpckg_classifier) {
        this.completedslpckg_classifier = completedslpckg_classifier;
    }

}