





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_ReferenceOperation extends FeatureOperation {

    private String oppositeFeatureName;
    private String containmentType;
    private boolean bidirectional;



    public esmodel_operations_ReferenceOperation(
        String oppositeFeatureName,        String containmentType,        boolean bidirectional    ) {
        super(
        );
        this.oppositeFeatureName = oppositeFeatureName;
        this.containmentType = containmentType;
        this.bidirectional = bidirectional;
    }


    public String getOppositefeaturename() {
        return oppositeFeatureName;
    }

    public void setOppositefeaturename(String oppositeFeatureName) {
        this.oppositeFeatureName = oppositeFeatureName;
    }
    public String getContainmenttype() {
        return containmentType;
    }

    public void setContainmenttype(String containmentType) {
        this.containmentType = containmentType;
    }
    public boolean getBidirectional() {
        return bidirectional;
    }

    public void setBidirectional(boolean bidirectional) {
        this.bidirectional = bidirectional;
    }


}