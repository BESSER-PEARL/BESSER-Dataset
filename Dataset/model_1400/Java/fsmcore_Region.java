





import java.util.List;
import java.util.ArrayList;

public class fsmcore_Region extends NamedElement {






    private List<fsmcore_AbstractState> fsmcore_abstractstates;




    private fsmcore_AbstractState fsmcore_abstractstate;




    private fsmcore_StateMachine fsmcore_statemachine;




    private List<fsmcore_Transition> fsmcore_transitions;


    public fsmcore_Region(
    ) {
        super(
        );
        this.fsmcore_abstractstates = new ArrayList<>();
        this.fsmcore_transitions = new ArrayList<>();
    }

    public fsmcore_Region(
        ArrayList<fsmcore_AbstractState> fsmcore_abstractstates,        ArrayList<fsmcore_Transition> fsmcore_transitions    ) {
        this.fsmcore_abstractstates = fsmcore_abstractstates;
        this.fsmcore_transitions = fsmcore_transitions;
    }


    public List<fsmcore_AbstractState> getFsmcore_abstractstates() {
        return fsmcore_abstractstates;
    }

    public void addFsmcore_abstractstate(Fsmcore_abstractstate fsmcore_abstractstate) {
        this.fsmcore_abstractstates.add(fsmcore_abstractstate);
    }
    public fsmcore_AbstractState getFsmcore_abstractstate() {
        return fsmcore_abstractstate;
    }

    public void setFsmcore_abstractstate(fsmcore_AbstractState fsmcore_abstractstate) {
        this.fsmcore_abstractstate = fsmcore_abstractstate;
    }
    public fsmcore_StateMachine getFsmcore_statemachine() {
        return fsmcore_statemachine;
    }

    public void setFsmcore_statemachine(fsmcore_StateMachine fsmcore_statemachine) {
        this.fsmcore_statemachine = fsmcore_statemachine;
    }
    public List<fsmcore_Transition> getFsmcore_transitions() {
        return fsmcore_transitions;
    }

    public void addFsmcore_transition(Fsmcore_transition fsmcore_transition) {
        this.fsmcore_transitions.add(fsmcore_transition);
    }

}