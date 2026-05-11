





import java.util.List;
import java.util.ArrayList;

public class Class_Attribute extends NamedElt {

    private boolean multiValued;





    private Class_Classifier class_classifier;


    public Class_Attribute(
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

    public Class_Classifier getClass_classifier() {
        return class_classifier;
    }

    public void setClass_classifier(Class_Classifier class_classifier) {
        this.class_classifier = class_classifier;
    }

}