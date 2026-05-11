





import java.util.List;
import java.util.ArrayList;

public class UML_14_AssociationEnd extends ModelElement {

    private String visibility;
    private boolean isNavigable;
    private String targetScope;
    private String changeability;
    private String aggregation;



    public UML_14_AssociationEnd(
        String visibility,        boolean isNavigable,        String targetScope,        String changeability,        String aggregation    ) {
        super(
        );
        this.visibility = visibility;
        this.isNavigable = isNavigable;
        this.targetScope = targetScope;
        this.changeability = changeability;
        this.aggregation = aggregation;
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
    public String getChangeability() {
        return changeability;
    }

    public void setChangeability(String changeability) {
        this.changeability = changeability;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }


}