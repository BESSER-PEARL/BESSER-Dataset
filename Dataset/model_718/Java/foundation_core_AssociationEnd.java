





import java.util.List;
import java.util.ArrayList;

public class foundation_core_AssociationEnd extends ModelElement {

    private String ordering;
    private String targetScope;
    private String isNavigable;
    private String aggregation;
    private String changeability;





    private Multiplicity_ multiplicity_;


    public foundation_core_AssociationEnd(
        String ordering,        String targetScope,        String isNavigable,        String aggregation,        String changeability    ) {
        super(
        );
        this.ordering = ordering;
        this.targetScope = targetScope;
        this.isNavigable = isNavigable;
        this.aggregation = aggregation;
        this.changeability = changeability;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public String getTargetscope() {
        return targetScope;
    }

    public void setTargetscope(String targetScope) {
        this.targetScope = targetScope;
    }
    public String getIsnavigable() {
        return isNavigable;
    }

    public void setIsnavigable(String isNavigable) {
        this.isNavigable = isNavigable;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
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

}