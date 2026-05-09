





import java.util.List;
import java.util.ArrayList;

public class fsmkerm_FSM  {






    private List<fsmkerm_Transition> fsmkerm_transitions;


    public fsmkerm_FSM(
    ) {
        this.fsmkerm_transitions = new ArrayList<>();
    }

    public fsmkerm_FSM(
        ArrayList<fsmkerm_Transition> fsmkerm_transitions    ) {
        this.fsmkerm_transitions = fsmkerm_transitions;
    }


    public List<fsmkerm_Transition> getFsmkerm_transitions() {
        return fsmkerm_transitions;
    }

    public void addFsmkerm_transition(Fsmkerm_transition fsmkerm_transition) {
        this.fsmkerm_transitions.add(fsmkerm_transition);
    }

}