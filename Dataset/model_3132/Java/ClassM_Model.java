





import java.util.List;
import java.util.ArrayList;

public class ClassM_Model  {






    private List<ClassM_Classifier> classm_classifiers;


    public ClassM_Model(
    ) {
        this.classm_classifiers = new ArrayList<>();
    }

    public ClassM_Model(
        ArrayList<ClassM_Classifier> classm_classifiers    ) {
        this.classm_classifiers = classm_classifiers;
    }


    public List<ClassM_Classifier> getClassm_classifiers() {
        return classm_classifiers;
    }

    public void addClassm_classifier(Classm_classifier classm_classifier) {
        this.classm_classifiers.add(classm_classifier);
    }

}