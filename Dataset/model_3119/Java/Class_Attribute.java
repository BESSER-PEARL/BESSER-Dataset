





import java.util.List;
import java.util.ArrayList;

public class Class_Attribute extends NamedElt {

    private String multiValued;





    private Class class;




    private Classifier classifier;


    public Class_Attribute(
        String multiValued    ) {
        super(
        );
        this.multiValued = multiValued;
    }


    public String getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(String multiValued) {
        this.multiValued = multiValued;
    }

    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}