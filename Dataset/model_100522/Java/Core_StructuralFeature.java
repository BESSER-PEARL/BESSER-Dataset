





import java.util.List;
import java.util.ArrayList;

public class Core_StructuralFeature extends Feature {

    private String changeability;
    private String targetScope;
    private String ordering;





    private Classifier classifier;


    public Core_StructuralFeature(
        String changeability,        String targetScope,        String ordering    ) {
        super(
        );
        this.changeability = changeability;
        this.targetScope = targetScope;
        this.ordering = ordering;
    }


    public String getChangeability() {
        return changeability;
    }

    public void setChangeability(String changeability) {
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

    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}