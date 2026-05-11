





import java.util.List;
import java.util.ArrayList;

public class model_Category extends BasicCode {

    private String classifier;
    private String associatedClassifier;



    public model_Category(
        String classifier,        String associatedClassifier    ) {
        super(
        );
        this.classifier = classifier;
        this.associatedClassifier = associatedClassifier;
    }


    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }
    public String getAssociatedclassifier() {
        return associatedClassifier;
    }

    public void setAssociatedclassifier(String associatedClassifier) {
        this.associatedClassifier = associatedClassifier;
    }


}