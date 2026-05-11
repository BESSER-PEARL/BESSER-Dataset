





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_GeneralizationSet extends PackageableElement {

    private boolean isCovering;
    private boolean isDisjoint;





    private ClassesProv_Generalization classesprov_generalization;




    private List<ClassesProv_Generalization> classesprov_generalizations;




    private ClassesProv_Classifier classesprov_classifier;




    private ClassesProv_Classifier classesprov_classifier;


    public ClassesProv_GeneralizationSet(
        boolean isCovering,        boolean isDisjoint    ) {
        super(
        );
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.classesprov_generalizations = new ArrayList<>();
    }

    public ClassesProv_GeneralizationSet(
        boolean isCovering,        boolean isDisjoint        ArrayList<ClassesProv_Generalization> classesprov_generalizations    ) {
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.classesprov_generalizations = classesprov_generalizations;
    }

    public boolean getIscovering() {
        return isCovering;
    }

    public void setIscovering(boolean isCovering) {
        this.isCovering = isCovering;
    }
    public boolean getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(boolean isDisjoint) {
        this.isDisjoint = isDisjoint;
    }

    public ClassesProv_Generalization getClassesprov_generalization() {
        return classesprov_generalization;
    }

    public void setClassesprov_generalization(ClassesProv_Generalization classesprov_generalization) {
        this.classesprov_generalization = classesprov_generalization;
    }
    public List<ClassesProv_Generalization> getClassesprov_generalizations() {
        return classesprov_generalizations;
    }

    public void addClassesprov_generalization(Classesprov_generalization classesprov_generalization) {
        this.classesprov_generalizations.add(classesprov_generalization);
    }
    public ClassesProv_Classifier getClassesprov_classifier() {
        return classesprov_classifier;
    }

    public void setClassesprov_classifier(ClassesProv_Classifier classesprov_classifier) {
        this.classesprov_classifier = classesprov_classifier;
    }
    public ClassesProv_Classifier getClassesprov_classifier() {
        return classesprov_classifier;
    }

    public void setClassesprov_classifier(ClassesProv_Classifier classesprov_classifier) {
        this.classesprov_classifier = classesprov_classifier;
    }

}