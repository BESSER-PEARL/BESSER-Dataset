





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_UnmarshallAction extends Action {






    private List<ActionsProv_OutputPin> actionsprov_outputpins;


    public ActionsProv_UnmarshallAction(
    ) {
        super(
        );
        this.actionsprov_outputpins = new ArrayList<>();
    }

    public ActionsProv_UnmarshallAction(
        ArrayList<ActionsProv_OutputPin> actionsprov_outputpins    ) {
        this.actionsprov_outputpins = actionsprov_outputpins;
    }


    public List<ActionsProv_OutputPin> getActionsprov_outputpins() {
        return actionsprov_outputpins;
    }

    public void addActionsprov_outputpin(Actionsprov_outputpin actionsprov_outputpin) {
        this.actionsprov_outputpins.add(actionsprov_outputpin);
    }

}