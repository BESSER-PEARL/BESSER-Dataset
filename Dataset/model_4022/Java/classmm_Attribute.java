





import java.util.List;
import java.util.ArrayList;

public class classmm_Attribute extends NamedElt {

    private String visibility;
    private boolean multivalued;





    private classmm_Classifier classmm_classifier;


    public classmm_Attribute(
        String visibility,        boolean multivalued    ) {
        super(
        );
        this.visibility = visibility;
        this.multivalued = multivalued;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }

    public classmm_Classifier getClassmm_classifier() {
        return classmm_classifier;
    }

    public void setClassmm_classifier(classmm_Classifier classmm_classifier) {
        this.classmm_classifier = classmm_classifier;
    }

}