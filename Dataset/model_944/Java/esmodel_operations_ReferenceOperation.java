





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_ReferenceOperation extends FeatureOperation {

    private String oppositeFeatureName;
    private boolean bidirectional;
    private String containmentType;



    public esmodel_operations_ReferenceOperation(
        String oppositeFeatureName,        boolean bidirectional,        String containmentType    ) {
        super(
        );
        this.oppositeFeatureName = oppositeFeatureName;
        this.bidirectional = bidirectional;
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
    public String getContainmenttype() {
        return containmentType;
    }

    public void setContainmenttype(String containmentType) {
        this.containmentType = containmentType;
    }


}