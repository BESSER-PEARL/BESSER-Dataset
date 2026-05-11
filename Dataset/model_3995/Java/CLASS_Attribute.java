





import java.util.List;
import java.util.ArrayList;

public class CLASS_Attribute extends NamedElement {

    private boolean multiValued;





    private CLASS_Classifier class_classifier;


    public CLASS_Attribute(
        boolean multiValued    ) {
        super(
        );
        this.multiValued = multiValued;
    }


    public boolean getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(boolean multiValued) {
        this.multiValued = multiValued;
    }

    public CLASS_Classifier getClass_classifier() {
        return class_classifier;
    }

    public void setClass_classifier(CLASS_Classifier class_classifier) {
        this.class_classifier = class_classifier;
    }

}