





import java.util.List;
import java.util.ArrayList;

public class simpleUML_MM_ClassModel  {






    private List<simpleUML_MM_Association> simpleuml_mm_associations;




    private List<simpleUML_MM_Classifier> simpleuml_mm_classifiers;


    public simpleUML_MM_ClassModel(
    ) {
        this.simpleuml_mm_associations = new ArrayList<>();
        this.simpleuml_mm_classifiers = new ArrayList<>();
    }

    public simpleUML_MM_ClassModel(
        ArrayList<simpleUML_MM_Association> simpleuml_mm_associations,        ArrayList<simpleUML_MM_Classifier> simpleuml_mm_classifiers    ) {
        this.simpleuml_mm_associations = simpleuml_mm_associations;
        this.simpleuml_mm_classifiers = simpleuml_mm_classifiers;
    }


    public List<simpleUML_MM_Association> getSimpleuml_mm_associations() {
        return simpleuml_mm_associations;
    }

    public void addSimpleuml_mm_association(Simpleuml_mm_association simpleuml_mm_association) {
        this.simpleuml_mm_associations.add(simpleuml_mm_association);
    }
    public List<simpleUML_MM_Classifier> getSimpleuml_mm_classifiers() {
        return simpleuml_mm_classifiers;
    }

    public void addSimpleuml_mm_classifier(Simpleuml_mm_classifier simpleuml_mm_classifier) {
        this.simpleuml_mm_classifiers.add(simpleuml_mm_classifier);
    }

}