





import java.util.List;
import java.util.ArrayList;

public class RefUML_Class extends Classifier {

    private String isActive;





    private List<RefUML_Class> refuml_classs;




    private List<RefUML_Classifier> refuml_classifiers;


    public RefUML_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.refuml_classs = new ArrayList<>();
        this.refuml_classifiers = new ArrayList<>();
    }

    public RefUML_Class(
        String isActive        ArrayList<RefUML_Class> refuml_classs,        ArrayList<RefUML_Classifier> refuml_classifiers    ) {
        this.isActive = isActive;
        this.refuml_classs = refuml_classs;
        this.refuml_classifiers = refuml_classifiers;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public List<RefUML_Class> getRefuml_classs() {
        return refuml_classs;
    }

    public void addRefuml_class(Refuml_class refuml_class) {
        this.refuml_classs.add(refuml_class);
    }
    public List<RefUML_Classifier> getRefuml_classifiers() {
        return refuml_classifiers;
    }

    public void addRefuml_classifier(Refuml_classifier refuml_classifier) {
        this.refuml_classifiers.add(refuml_classifier);
    }

}