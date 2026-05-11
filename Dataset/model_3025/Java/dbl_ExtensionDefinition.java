





import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensionDefinition extends LanguageConceptClassifier, ExtensibleElement {






    private dbl_Module dbl_module;




    private List<dbl_Classifier> dbl_classifiers;


    public dbl_ExtensionDefinition(
    ) {
        super(
        );
        this.dbl_classifiers = new ArrayList<>();
    }

    public dbl_ExtensionDefinition(
        ArrayList<dbl_Classifier> dbl_classifiers    ) {
        this.dbl_classifiers = dbl_classifiers;
    }


    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }
    public List<dbl_Classifier> getDbl_classifiers() {
        return dbl_classifiers;
    }

    public void addDbl_classifier(Dbl_classifier dbl_classifier) {
        this.dbl_classifiers.add(dbl_classifier);
    }

}