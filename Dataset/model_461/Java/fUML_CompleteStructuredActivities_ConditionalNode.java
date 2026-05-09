





import java.util.List;
import java.util.ArrayList;

public class fUML_CompleteStructuredActivities_ConditionalNode extends StructuredActivityNode {

    private boolean assured;
    private boolean determinate;



    public fUML_CompleteStructuredActivities_ConditionalNode(
        boolean assured,        boolean determinate    ) {
        super(
        );
        this.assured = assured;
        this.determinate = determinate;
    }


    public boolean getAssured() {
        return assured;
    }

    public void setAssured(boolean assured) {
        this.assured = assured;
    }
    public boolean getDeterminate() {
        return determinate;
    }

    public void setDeterminate(boolean determinate) {
        this.determinate = determinate;
    }


}