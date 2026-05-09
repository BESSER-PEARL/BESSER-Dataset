





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteStructuredActivities_ConditionalNode extends StructuredActivityNode {

    private boolean determinate;
    private boolean assured;



    public xmof_CompleteStructuredActivities_ConditionalNode(
        boolean determinate,        boolean assured    ) {
        super(
        );
        this.determinate = determinate;
        this.assured = assured;
    }


    public boolean getDeterminate() {
        return determinate;
    }

    public void setDeterminate(boolean determinate) {
        this.determinate = determinate;
    }
    public boolean getAssured() {
        return assured;
    }

    public void setAssured(boolean assured) {
        this.assured = assured;
    }


}