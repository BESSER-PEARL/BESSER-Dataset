





import java.util.List;
import java.util.ArrayList;

public class umlClass_Package extends NamedElement {






    private List<umlClass_Classifier> umlclass_classifiers;




    private umlClass_Classifier umlclass_classifier;


    public umlClass_Package(
    ) {
        super(
        );
        this.umlclass_classifiers = new ArrayList<>();
    }

    public umlClass_Package(
        ArrayList<umlClass_Classifier> umlclass_classifiers    ) {
        this.umlclass_classifiers = umlclass_classifiers;
    }


    public List<umlClass_Classifier> getUmlclass_classifiers() {
        return umlclass_classifiers;
    }

    public void addUmlclass_classifier(Umlclass_classifier umlclass_classifier) {
        this.umlclass_classifiers.add(umlclass_classifier);
    }
    public umlClass_Classifier getUmlclass_classifier() {
        return umlclass_classifier;
    }

    public void setUmlclass_classifier(umlClass_Classifier umlclass_classifier) {
        this.umlclass_classifier = umlclass_classifier;
    }

}