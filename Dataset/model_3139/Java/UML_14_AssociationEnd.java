





import java.util.List;
import java.util.ArrayList;

public class UML_14_AssociationEnd extends ModelElement {

    private boolean isNavigable;
    private String targetScope;
    private String visibility;
    private String aggregation;
    private String changeability;



    public UML_14_AssociationEnd(
        boolean isNavigable,        String targetScope,        String visibility,        String aggregation,        String changeability    ) {
        super(
        );
        this.isNavigable = isNavigable;
        this.targetScope = targetScope;
        this.visibility = visibility;
        this.aggregation = aggregation;
        this.changeability = changeability;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
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


}