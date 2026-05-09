





import java.util.List;
import java.util.ArrayList;

public class fsmcore_StateMachine extends NamedElement {






    private List<fsmcore_State> fsmcore_states;




    private List<fsmcore_Transition> fsmcore_transitions;


    public fsmcore_StateMachine(
    ) {
        super(
        );
        this.fsmcore_states = new ArrayList<>();
        this.fsmcore_transitions = new ArrayList<>();
    }

    public fsmcore_StateMachine(
        ArrayList<fsmcore_State> fsmcore_states,        ArrayList<fsmcore_Transition> fsmcore_transitions    ) {
        this.fsmcore_states = fsmcore_states;
        this.fsmcore_transitions = fsmcore_transitions;
    }


    public List<fsmcore_State> getFsmcore_states() {
        return fsmcore_states;
    }

    public void addFsmcore_state(Fsmcore_state fsmcore_state) {
        this.fsmcore_states.add(fsmcore_state);
    }
    public List<fsmcore_Transition> getFsmcore_transitions() {
        return fsmcore_transitions;
    }

    public void addFsmcore_transition(Fsmcore_transition fsmcore_transition) {
        this.fsmcore_transitions.add(fsmcore_transition);
    }

}