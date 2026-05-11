





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_Action  {






    private List<ActionsProv_OutputPin> actionsprov_outputpins;




    private ActionsProv_ActionInputPin actionsprov_actioninputpin;




    private List<ActionsProv_InputPin> actionsprov_inputpins;


    public ActionsProv_Action(
    ) {
        this.actionsprov_outputpins = new ArrayList<>();
        this.actionsprov_inputpins = new ArrayList<>();
    }

    public ActionsProv_Action(
        ArrayList<ActionsProv_OutputPin> actionsprov_outputpins,        ArrayList<ActionsProv_InputPin> actionsprov_inputpins    ) {
        this.actionsprov_outputpins = actionsprov_outputpins;
        this.actionsprov_inputpins = actionsprov_inputpins;
    }


    public List<ActionsProv_OutputPin> getActionsprov_outputpins() {
        return actionsprov_outputpins;
    }

    public void addActionsprov_outputpin(Actionsprov_outputpin actionsprov_outputpin) {
        this.actionsprov_outputpins.add(actionsprov_outputpin);
    }
    public ActionsProv_ActionInputPin getActionsprov_actioninputpin() {
        return actionsprov_actioninputpin;
    }

    public void setActionsprov_actioninputpin(ActionsProv_ActionInputPin actionsprov_actioninputpin) {
        this.actionsprov_actioninputpin = actionsprov_actioninputpin;
    }
    public List<ActionsProv_InputPin> getActionsprov_inputpins() {
        return actionsprov_inputpins;
    }

    public void addActionsprov_inputpin(Actionsprov_inputpin actionsprov_inputpin) {
        this.actionsprov_inputpins.add(actionsprov_inputpin);
    }

}