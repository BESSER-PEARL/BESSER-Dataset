





import java.util.List;
import java.util.ArrayList;

public class classes_Property extends StructuralFeature {

    private boolean composite;
    private boolean derived;
    private String aggregation;
    private boolean derivedUnion;





    private classes_Property classes_property;




    private classes_Classifier classes_classifier;


    public classes_Property(
        boolean composite,        boolean derived,        String aggregation,        boolean derivedUnion    ) {
        super(
        );
        this.composite = composite;
        this.derived = derived;
        this.aggregation = aggregation;
        this.derivedUnion = derivedUnion;
    }


    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public boolean getDerivedunion() {
        return derivedUnion;
    }

    public void setDerivedunion(boolean derivedUnion) {
        this.derivedUnion = derivedUnion;
    }

    public classes_Property getClasses_property() {
        return classes_property;
    }

    public void setClasses_property(classes_Property classes_property) {
        this.classes_property = classes_property;
    }
    public classes_Classifier getClasses_classifier() {
        return classes_classifier;
    }

    public void setClasses_classifier(classes_Classifier classes_classifier) {
        this.classes_classifier = classes_classifier;
    }

}