





import java.util.List;
import java.util.ArrayList;

public class foundation_core_StructuralFeature extends Feature {

    private String targetScope;
    private String ordering;
    private String changeability;





    private Multiplicity_ multiplicity_;




    private Classifier classifier;


    public foundation_core_StructuralFeature(
        String targetScope,        String ordering,        String changeability    ) {
        super(
        );
        this.targetScope = targetScope;
        this.ordering = ordering;
        this.changeability = changeability;
    }


    public String getTargetscope() {
        return targetScope;
    }

    public void setTargetscope(String targetScope) {
        this.targetScope = targetScope;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public String getChangeability() {
        return changeability;
    }

    public void setChangeability(String changeability) {
        this.changeability = changeability;
    }

    public Multiplicity_ getMultiplicity_() {
        return multiplicity_;
    }

    public void setMultiplicity_(Multiplicity_ multiplicity_) {
        this.multiplicity_ = multiplicity_;
    }
    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}