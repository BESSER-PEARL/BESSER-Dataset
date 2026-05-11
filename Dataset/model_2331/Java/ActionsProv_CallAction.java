





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_CallAction extends InvocationAction {

    private boolean isSynchronous;





    private List<ActionsProv_OutputPin> actionsprov_outputpins;


    public ActionsProv_CallAction(
        boolean isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.actionsprov_outputpins = new ArrayList<>();
    }

    public ActionsProv_CallAction(
        boolean isSynchronous        ArrayList<ActionsProv_OutputPin> actionsprov_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.actionsprov_outputpins = actionsprov_outputpins;
    }

    public boolean getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(boolean isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<ActionsProv_OutputPin> getActionsprov_outputpins() {
        return actionsprov_outputpins;
    }

    public void addActionsprov_outputpin(Actionsprov_outputpin actionsprov_outputpin) {
        this.actionsprov_outputpins.add(actionsprov_outputpin);
    }

}