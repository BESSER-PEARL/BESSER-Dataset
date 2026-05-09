





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteStructuredActivities_LoopNode extends StructuredActivityNode {

    private boolean testedFirst;



    public xmof_CompleteStructuredActivities_LoopNode(
        boolean testedFirst    ) {
        super(
        );
        this.testedFirst = testedFirst;
    }


    public boolean getTestedfirst() {
        return testedFirst;
    }

    public void setTestedfirst(boolean testedFirst) {
        this.testedFirst = testedFirst;
    }


}