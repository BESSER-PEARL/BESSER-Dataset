





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_ReduceAction extends Action {

    private boolean isOrdered;





    private ActionsProv_OutputPin actionsprov_outputpin;


    public ActionsProv_ReduceAction(
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

    public ActionsProv_OutputPin getActionsprov_outputpin() {
        return actionsprov_outputpin;
    }

    public void setActionsprov_outputpin(ActionsProv_OutputPin actionsprov_outputpin) {
        this.actionsprov_outputpin = actionsprov_outputpin;
    }

}