





import java.util.List;
import java.util.ArrayList;

public class Activities_StructuredActivities_LoopNode extends StructuredActivityNode {

    private boolean isTestedFirst;



    public Activities_StructuredActivities_LoopNode(
        boolean isTestedFirst    ) {
        super(
        );
        this.isTestedFirst = isTestedFirst;
    }


    public boolean getIstestedfirst() {
        return isTestedFirst;
    }

    public void setIstestedfirst(boolean isTestedFirst) {
        this.isTestedFirst = isTestedFirst;
    }


}