





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Feature extends RedefinableElement {

    private String isStatic;





    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private uml3_0_0_Classifier uml3_0_0_classifier;


    public uml3_0_0_Feature(
        String isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.uml3_0_0_classifiers = new ArrayList<>();
    }

    public uml3_0_0_Feature(
        String isStatic        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers    ) {
        this.isStatic = isStatic;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
    }

    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }

    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }

}