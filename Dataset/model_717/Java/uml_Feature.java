





import java.util.List;
import java.util.ArrayList;

public class uml_Feature  {

    private String isStatic;





    private uml_Classifier uml_classifier;




    private List<uml_Classifier> uml_classifiers;


    public uml_Feature(
        String isStatic    ) {
        this.isStatic = isStatic;
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_Feature(
        String isStatic        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.isStatic = isStatic;
        this.uml_classifiers = uml_classifiers;
    }

    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }

    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}