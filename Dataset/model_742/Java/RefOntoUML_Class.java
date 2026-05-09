





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Class extends Classifier {

    private String isActive;





    private RefOntoUML_Class refontouml_class;




    private List<RefOntoUML_Classifier> refontouml_classifiers;


    public RefOntoUML_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.refontouml_classifiers = new ArrayList<>();
    }

    public RefOntoUML_Class(
        String isActive        ArrayList<RefOntoUML_Classifier> refontouml_classifiers    ) {
        this.isActive = isActive;
        this.refontouml_classifiers = refontouml_classifiers;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public RefOntoUML_Class getRefontouml_class() {
        return refontouml_class;
    }

    public void setRefontouml_class(RefOntoUML_Class refontouml_class) {
        this.refontouml_class = refontouml_class;
    }
    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }

}