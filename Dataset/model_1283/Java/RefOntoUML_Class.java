





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Class extends Classifier {

    private String isActive;





    private List<RefOntoUML_Classifier> refontouml_classifiers;




    private List<RefOntoUML_Class> refontouml_classs;


    public RefOntoUML_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.refontouml_classifiers = new ArrayList<>();
        this.refontouml_classs = new ArrayList<>();
    }

    public RefOntoUML_Class(
        String isActive        ArrayList<RefOntoUML_Classifier> refontouml_classifiers,        ArrayList<RefOntoUML_Class> refontouml_classs    ) {
        this.isActive = isActive;
        this.refontouml_classifiers = refontouml_classifiers;
        this.refontouml_classs = refontouml_classs;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }
    public List<RefOntoUML_Class> getRefontouml_classs() {
        return refontouml_classs;
    }

    public void addRefontouml_class(Refontouml_class refontouml_class) {
        this.refontouml_classs.add(refontouml_class);
    }

}