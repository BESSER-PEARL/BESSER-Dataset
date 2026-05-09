





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Feature extends RedefinableElement {

    private String isStatic;





    private List<RefOntoUML_Classifier> refontouml_classifiers;




    private RefOntoUML_Classifier refontouml_classifier;


    public RefOntoUML_Feature(
        String isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.refontouml_classifiers = new ArrayList<>();
    }

    public RefOntoUML_Feature(
        String isStatic        ArrayList<RefOntoUML_Classifier> refontouml_classifiers    ) {
        this.isStatic = isStatic;
        this.refontouml_classifiers = refontouml_classifiers;
    }

    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }

    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }
    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }

}