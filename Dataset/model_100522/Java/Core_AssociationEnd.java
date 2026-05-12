





import java.util.List;
import java.util.ArrayList;

public class Core_AssociationEnd extends ModelElement {

    private String targetScope;
    private String aggregation;
    private String isNavigable;
    private String changeability;
    private String ordering;





    private List<Classifier> classifiers;




    private Classifier classifier;


    public Core_AssociationEnd(
        String targetScope,        String aggregation,        String isNavigable,        String changeability,        String ordering    ) {
        super(
        );
        this.targetScope = targetScope;
        this.aggregation = aggregation;
        this.isNavigable = isNavigable;
        this.changeability = changeability;
        this.ordering = ordering;
        this.classifiers = new ArrayList<>();
    }

    public Core_AssociationEnd(
        String targetScope,        String aggregation,        String isNavigable,        String changeability,        String ordering        ArrayList<Classifier> classifiers    ) {
        this.targetScope = targetScope;
        this.aggregation = aggregation;
        this.isNavigable = isNavigable;
        this.changeability = changeability;
        this.ordering = ordering;
        this.classifiers = classifiers;
    }

    public String getTargetscope() {
        return targetScope;
    }

    public void setTargetscope(String targetScope) {
        this.targetScope = targetScope;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getIsnavigable() {
        return isNavigable;
    }

    public void setIsnavigable(String isNavigable) {
        this.isNavigable = isNavigable;
    }
    public String getChangeability() {
        return changeability;
    }

    public void setChangeability(String changeability) {
        this.changeability = changeability;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public List<Classifier> getClassifiers() {
        return classifiers;
    }

    public void addClassifier(Classifier classifier) {
        this.classifiers.add(classifier);
    }
    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}