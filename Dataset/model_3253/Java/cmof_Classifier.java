





import java.util.List;
import java.util.ArrayList;

public class cmof_Classifier extends Type, Namespace {






    private List<cmof_Classifier> cmof_classifiers;


    public cmof_Classifier(
    ) {
        super(
        );
        this.cmof_classifiers = new ArrayList<>();
    }

    public cmof_Classifier(
        ArrayList<cmof_Classifier> cmof_classifiers    ) {
        this.cmof_classifiers = cmof_classifiers;
    }


    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }

}