





import java.util.List;
import java.util.ArrayList;

public class classes_CModel  {






    private List<classes_Classifier> classes_classifiers;


    public classes_CModel(
    ) {
        this.classes_classifiers = new ArrayList<>();
    }

    public classes_CModel(
        ArrayList<classes_Classifier> classes_classifiers    ) {
        this.classes_classifiers = classes_classifiers;
    }


    public List<classes_Classifier> getClasses_classifiers() {
        return classes_classifiers;
    }

    public void addClasses_classifier(Classes_classifier classes_classifier) {
        this.classes_classifiers.add(classes_classifier);
    }

}