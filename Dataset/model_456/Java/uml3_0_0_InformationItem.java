





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_InformationItem extends Classifier {






    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;


    public uml3_0_0_InformationItem(
    ) {
        super(
        );
        this.uml3_0_0_classifiers = new ArrayList<>();
    }

    public uml3_0_0_InformationItem(
        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers    ) {
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
    }


    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }

}