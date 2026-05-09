





import java.util.List;
import java.util.ArrayList;

public class fsmcore_Region extends NamedElement {






    private List<fsmcore_Transition> fsmcore_transitions;




    private fsmcore_StateMachine fsmcore_statemachine;


    public fsmcore_Region(
    ) {
        super(
        );
        this.fsmcore_transitions = new ArrayList<>();
    }

    public fsmcore_Region(
        ArrayList<fsmcore_Transition> fsmcore_transitions    ) {
        this.fsmcore_transitions = fsmcore_transitions;
    }


    public List<fsmcore_Transition> getFsmcore_transitions() {
        return fsmcore_transitions;
    }

    public void addFsmcore_transition(Fsmcore_transition fsmcore_transition) {
        this.fsmcore_transitions.add(fsmcore_transition);
    }
    public fsmcore_StateMachine getFsmcore_statemachine() {
        return fsmcore_statemachine;
    }

    public void setFsmcore_statemachine(fsmcore_StateMachine fsmcore_statemachine) {
        this.fsmcore_statemachine = fsmcore_statemachine;
    }

}