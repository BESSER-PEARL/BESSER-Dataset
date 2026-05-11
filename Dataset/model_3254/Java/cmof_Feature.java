





import java.util.List;
import java.util.ArrayList;

public class cmof_Feature extends RedefinableElement {






    private cmof_Classifier cmof_classifier;




    private List<cmof_Classifier> cmof_classifiers;


    public cmof_Feature(
    ) {
        super(
        );
        this.cmof_classifiers = new ArrayList<>();
    }

    public cmof_Feature(
        ArrayList<cmof_Classifier> cmof_classifiers    ) {
        this.cmof_classifiers = cmof_classifiers;
    }


    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }
    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }

}