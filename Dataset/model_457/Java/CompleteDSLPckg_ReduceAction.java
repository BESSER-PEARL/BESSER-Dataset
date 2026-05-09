





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ReduceAction extends Action {

    private boolean isOrdered;





    private CompleteDSLPckg_Behavior completedslpckg_behavior;


    public CompleteDSLPckg_ReduceAction(
        boolean isOrdered    ) {
        super(
        );
        this.isOrdered = isOrdered;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }

    public CompleteDSLPckg_Behavior getCompletedslpckg_behavior() {
        return completedslpckg_behavior;
    }

    public void setCompletedslpckg_behavior(CompleteDSLPckg_Behavior completedslpckg_behavior) {
        this.completedslpckg_behavior = completedslpckg_behavior;
    }

}