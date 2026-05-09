





import java.util.List;
import java.util.ArrayList;

public class uml_InformationItem extends Classifier {






    private List<uml_Classifier> uml_classifiers;


    public uml_InformationItem(
    ) {
        super(
        );
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_InformationItem(
        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.uml_classifiers = uml_classifiers;
    }


    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}