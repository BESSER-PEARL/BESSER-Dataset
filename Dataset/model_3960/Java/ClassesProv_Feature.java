





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Feature extends RedefinableElement {

    private boolean isStatic;





    private List<ClassesProv_Classifier> classesprov_classifiers;




    private ClassesProv_Classifier classesprov_classifier;


    public ClassesProv_Feature(
        boolean isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.classesprov_classifiers = new ArrayList<>();
    }

    public ClassesProv_Feature(
        boolean isStatic        ArrayList<ClassesProv_Classifier> classesprov_classifiers    ) {
        this.isStatic = isStatic;
        this.classesprov_classifiers = classesprov_classifiers;
    }

    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public List<ClassesProv_Classifier> getClassesprov_classifiers() {
        return classesprov_classifiers;
    }

    public void addClassesprov_classifier(Classesprov_classifier classesprov_classifier) {
        this.classesprov_classifiers.add(classesprov_classifier);
    }
    public ClassesProv_Classifier getClassesprov_classifier() {
        return classesprov_classifier;
    }

    public void setClassesprov_classifier(ClassesProv_Classifier classesprov_classifier) {
        this.classesprov_classifier = classesprov_classifier;
    }

}