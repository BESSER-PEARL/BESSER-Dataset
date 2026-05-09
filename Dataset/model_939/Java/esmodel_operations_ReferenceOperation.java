





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_ReferenceOperation extends FeatureOperation {

    private String containmentType;
    private String oppositeFeatureName;
    private boolean bidirectional;



    public esmodel_operations_ReferenceOperation(
        String containmentType,        String oppositeFeatureName,        boolean bidirectional    ) {
        super(
        );
        this.containmentType = containmentType;
        this.oppositeFeatureName = oppositeFeatureName;
        this.bidirectional = bidirectional;
    }


    public String getContainmenttype() {
        return containmentType;
    }

    public void setContainmenttype(String containmentType) {
        this.containmentType = containmentType;
    }
    public String getOppositefeaturename() {
        return oppositeFeatureName;
    }

    public void setOppositefeaturename(String oppositeFeatureName) {
        this.oppositeFeatureName = oppositeFeatureName;
    }
    public boolean getBidirectional() {
        return bidirectional;
    }

    public void setBidirectional(boolean bidirectional) {
        this.bidirectional = bidirectional;
    }


}