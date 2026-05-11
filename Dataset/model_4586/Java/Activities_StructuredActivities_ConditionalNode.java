





import java.util.List;
import java.util.ArrayList;

public class Activities_StructuredActivities_ConditionalNode extends StructuredActivityNode {

    private boolean isDeterminate;
    private boolean isAssumed;



    public Activities_StructuredActivities_ConditionalNode(
        boolean isDeterminate,        boolean isAssumed    ) {
        super(
        );
        this.isDeterminate = isDeterminate;
        this.isAssumed = isAssumed;
    }


    public boolean getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(boolean isDeterminate) {
        this.isDeterminate = isDeterminate;
    }
    public boolean getIsassumed() {
        return isAssumed;
    }

    public void setIsassumed(boolean isAssumed) {
        this.isAssumed = isAssumed;
    }


}