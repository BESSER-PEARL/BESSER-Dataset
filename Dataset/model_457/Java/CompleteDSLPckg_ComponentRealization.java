





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ComponentRealization extends Realization {






    private CompleteDSLPckg_Component completedslpckg_component;




    private CompleteDSLPckg_Component completedslpckg_component;




    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;


    public CompleteDSLPckg_ComponentRealization(
    ) {
        super(
        );
        this.completedslpckg_classifiers = new ArrayList<>();
    }

    public CompleteDSLPckg_ComponentRealization(
        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers    ) {
        this.completedslpckg_classifiers = completedslpckg_classifiers;
    }


    public CompleteDSLPckg_Component getCompletedslpckg_component() {
        return completedslpckg_component;
    }

    public void setCompletedslpckg_component(CompleteDSLPckg_Component completedslpckg_component) {
        this.completedslpckg_component = completedslpckg_component;
    }
    public CompleteDSLPckg_Component getCompletedslpckg_component() {
        return completedslpckg_component;
    }

    public void setCompletedslpckg_component(CompleteDSLPckg_Component completedslpckg_component) {
        this.completedslpckg_component = completedslpckg_component;
    }
    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }

}