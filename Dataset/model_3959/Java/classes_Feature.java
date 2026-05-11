





import java.util.List;
import java.util.ArrayList;

public class classes_Feature extends RedefinableElement {

    private boolean static;





    private List<classes_Classifier> classes_classifiers;




    private classes_Classifier classes_classifier;


    public classes_Feature(
        boolean static    ) {
        super(
        );
        this.static = static;
        this.classes_classifiers = new ArrayList<>();
    }

    public classes_Feature(
        boolean static        ArrayList<classes_Classifier> classes_classifiers    ) {
        this.static = static;
        this.classes_classifiers = classes_classifiers;
    }

    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public List<classes_Classifier> getClasses_classifiers() {
        return classes_classifiers;
    }

    public void addClasses_classifier(Classes_classifier classes_classifier) {
        this.classes_classifiers.add(classes_classifier);
    }
    public classes_Classifier getClasses_classifier() {
        return classes_classifier;
    }

    public void setClasses_classifier(classes_Classifier classes_classifier) {
        this.classes_classifier = classes_classifier;
    }

}