





import java.util.List;
import java.util.ArrayList;

public class UML_14_AssociationEnd extends ModelElement {

    private String changeability;
    private String visibility;
    private boolean isNavigable;
    private String targetScope;
    private String aggregation;



    public UML_14_AssociationEnd(
        String changeability,        String visibility,        boolean isNavigable,        String targetScope,        String aggregation    ) {
        super(
        );
        this.changeability = changeability;
        this.visibility = visibility;
        this.isNavigable = isNavigable;
        this.targetScope = targetScope;
        this.aggregation = aggregation;
    }


    public String getChangeability() {
        return changeability;
    }

    public void setChangeability(String changeability) {
        this.changeability = changeability;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getIsnavigable() {
        return isNavigable;
    }

    public void setIsnavigable(boolean isNavigable) {
        this.isNavigable = isNavigable;
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


}