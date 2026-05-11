





import java.util.List;
import java.util.ArrayList;

public class simpleUML_Classifier extends NamedElement {






    private simpleUML_Attribute simpleuml_attribute;




    private List<simpleUML_Classifier> simpleuml_classifiers;




    private simpleUML_Classifier simpleuml_classifier;


    public simpleUML_Classifier(
    ) {
        super(
        );
        this.simpleuml_classifiers = new ArrayList<>();
    }

    public simpleUML_Classifier(
        ArrayList<simpleUML_Classifier> simpleuml_classifiers    ) {
        this.simpleuml_classifiers = simpleuml_classifiers;
    }


    public simpleUML_Attribute getSimpleuml_attribute() {
        return simpleuml_attribute;
    }

    public void setSimpleuml_attribute(simpleUML_Attribute simpleuml_attribute) {
        this.simpleuml_attribute = simpleuml_attribute;
    }
    public List<simpleUML_Classifier> getSimpleuml_classifiers() {
        return simpleuml_classifiers;
    }

    public void addSimpleuml_classifier(Simpleuml_classifier simpleuml_classifier) {
        this.simpleuml_classifiers.add(simpleuml_classifier);
    }
    public simpleUML_Classifier getSimpleuml_classifier() {
        return simpleuml_classifier;
    }

    public void setSimpleuml_classifier(simpleUML_Classifier simpleuml_classifier) {
        this.simpleuml_classifier = simpleuml_classifier;
    }

}