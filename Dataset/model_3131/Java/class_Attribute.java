





import java.util.List;
import java.util.ArrayList;

public class class_Attribute extends NamedElt {

    private boolean multiValued;





    private class_Classifier class_classifier;


    public class_Attribute(
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

    public class_Classifier getClass_classifier() {
        return class_classifier;
    }

    public void setClass_classifier(class_Classifier class_classifier) {
        this.class_classifier = class_classifier;
    }

}