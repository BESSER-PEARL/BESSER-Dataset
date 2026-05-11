





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Feature  {






    private List<uml2CD_Classifier> uml2cd_classifiers;




    private uml2CD_Classifier uml2cd_classifier;


    public uml2CD_Feature(
    ) {
        this.uml2cd_classifiers = new ArrayList<>();
    }

    public uml2CD_Feature(
        ArrayList<uml2CD_Classifier> uml2cd_classifiers    ) {
        this.uml2cd_classifiers = uml2cd_classifiers;
    }


    public List<uml2CD_Classifier> getUml2cd_classifiers() {
        return uml2cd_classifiers;
    }

    public void addUml2cd_classifier(Uml2cd_classifier uml2cd_classifier) {
        this.uml2cd_classifiers.add(uml2cd_classifier);
    }
    public uml2CD_Classifier getUml2cd_classifier() {
        return uml2cd_classifier;
    }

    public void setUml2cd_classifier(uml2CD_Classifier uml2cd_classifier) {
        this.uml2cd_classifier = uml2cd_classifier;
    }

}