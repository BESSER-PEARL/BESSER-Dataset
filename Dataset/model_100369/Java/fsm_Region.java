





import java.util.List;
import java.util.ArrayList;

public class fsm_Region extends NamedElement {






    private List<fsm_Transition> fsm_transitions;




    private fsm_AbstractState fsm_abstractstate;




    private fsm_StateMachine fsm_statemachine;




    private List<fsm_AbstractState> fsm_abstractstates;


    public fsm_Region(
    ) {
        super(
        );
        this.fsm_transitions = new ArrayList<>();
        this.fsm_abstractstates = new ArrayList<>();
    }

    public fsm_Region(
        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_AbstractState> fsm_abstractstates    ) {
        this.fsm_transitions = fsm_transitions;
        this.fsm_abstractstates = fsm_abstractstates;
    }


    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public fsm_AbstractState getFsm_abstractstate() {
        return fsm_abstractstate;
    }

    public void setFsm_abstractstate(fsm_AbstractState fsm_abstractstate) {
        this.fsm_abstractstate = fsm_abstractstate;
    }
    public fsm_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(fsm_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public List<fsm_AbstractState> getFsm_abstractstates() {
        return fsm_abstractstates;
    }

    public void addFsm_abstractstate(Fsm_abstractstate fsm_abstractstate) {
        this.fsm_abstractstates.add(fsm_abstractstate);
    }

}