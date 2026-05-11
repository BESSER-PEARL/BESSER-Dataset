





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_AcceptEventAction extends Action {

    private boolean isUnmarshall;





    private List<ActionsProv_OutputPin> actionsprov_outputpins;


    public ActionsProv_AcceptEventAction(
        boolean isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
        this.actionsprov_outputpins = new ArrayList<>();
    }

    public ActionsProv_AcceptEventAction(
        boolean isUnmarshall        ArrayList<ActionsProv_OutputPin> actionsprov_outputpins    ) {
        this.isUnmarshall = isUnmarshall;
        this.actionsprov_outputpins = actionsprov_outputpins;
    }

    public boolean getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(boolean isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }

    public List<ActionsProv_OutputPin> getActionsprov_outputpins() {
        return actionsprov_outputpins;
    }

    public void addActionsprov_outputpin(Actionsprov_outputpin actionsprov_outputpin) {
        this.actionsprov_outputpins.add(actionsprov_outputpin);
    }

}