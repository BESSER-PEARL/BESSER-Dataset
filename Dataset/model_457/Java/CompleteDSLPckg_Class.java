





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Class extends StructuredClassifier, EncapsulatedClassifier, Classifier, BehavioredClassifier {






    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;




    private List<CompleteDSLPckg_Property> completedslpckg_propertys;




    private CompleteDSLPckg_Class completedslpckg_class;




    private CompleteDSLPckg_Property completedslpckg_property;


    public CompleteDSLPckg_Class(
    ) {
        super(
        );
        this.completedslpckg_classifiers = new ArrayList<>();
        this.completedslpckg_propertys = new ArrayList<>();
    }

    public CompleteDSLPckg_Class(
        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers,        ArrayList<CompleteDSLPckg_Property> completedslpckg_propertys    ) {
        this.completedslpckg_classifiers = completedslpckg_classifiers;
        this.completedslpckg_propertys = completedslpckg_propertys;
    }


    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }
    public List<CompleteDSLPckg_Property> getCompletedslpckg_propertys() {
        return completedslpckg_propertys;
    }

    public void addCompletedslpckg_property(Completedslpckg_property completedslpckg_property) {
        this.completedslpckg_propertys.add(completedslpckg_property);
    }
    public CompleteDSLPckg_Class getCompletedslpckg_class() {
        return completedslpckg_class;
    }

    public void setCompletedslpckg_class(CompleteDSLPckg_Class completedslpckg_class) {
        this.completedslpckg_class = completedslpckg_class;
    }
    public CompleteDSLPckg_Property getCompletedslpckg_property() {
        return completedslpckg_property;
    }

    public void setCompletedslpckg_property(CompleteDSLPckg_Property completedslpckg_property) {
        this.completedslpckg_property = completedslpckg_property;
    }

}