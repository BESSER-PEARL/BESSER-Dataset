





import java.util.List;
import java.util.ArrayList;

public class ClassMM_ClassModel  {






    private List<ClassMM_Classifier> classmm_classifiers;


    public ClassMM_ClassModel(
    ) {
        this.classmm_classifiers = new ArrayList<>();
    }

    public ClassMM_ClassModel(
        ArrayList<ClassMM_Classifier> classmm_classifiers    ) {
        this.classmm_classifiers = classmm_classifiers;
    }


    public List<ClassMM_Classifier> getClassmm_classifiers() {
        return classmm_classifiers;
    }

    public void addClassmm_classifier(Classmm_classifier classmm_classifier) {
        this.classmm_classifiers.add(classmm_classifier);
    }

}