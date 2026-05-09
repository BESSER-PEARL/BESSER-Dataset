





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {






    private List<fsm_Transition> fsm_transitions;




    private fsm_State fsm_state;




    private List<fsm_State> fsm_states;




    private fsm_State fsm_state;


    public fsm_StateMachine(
    ) {
        super(
        );
        this.fsm_transitions = new ArrayList<>();
        this.fsm_states = new ArrayList<>();
    }

    public fsm_StateMachine(
        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_State> fsm_states    ) {
        this.fsm_transitions = fsm_transitions;
        this.fsm_states = fsm_states;
    }


    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}