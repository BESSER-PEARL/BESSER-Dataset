





import java.util.List;
import java.util.ArrayList;

public class aadl2_ClassifierFeature extends NamedElement {






    private aadl2_Classifier aadl2_classifier;




    private List<aadl2_Classifier> aadl2_classifiers;


    public aadl2_ClassifierFeature(
    ) {
        super(
        );
        this.aadl2_classifiers = new ArrayList<>();
    }

    public aadl2_ClassifierFeature(
        ArrayList<aadl2_Classifier> aadl2_classifiers    ) {
        this.aadl2_classifiers = aadl2_classifiers;
    }


    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public List<aadl2_Classifier> getAadl2_classifiers() {
        return aadl2_classifiers;
    }

    public void addAadl2_classifier(Aadl2_classifier aadl2_classifier) {
        this.aadl2_classifiers.add(aadl2_classifier);
    }

}