





import java.util.List;
import java.util.ArrayList;

public class FSM_StateMachine extends MgaObject {






    private FSM_Transition fsm_transition;




    private List<FSM_State> fsm_states;




    private FSM_State fsm_state;




    private List<FSM_Transition> fsm_transitions;


    public FSM_StateMachine(
    ) {
        super(
        );
        this.fsm_states = new ArrayList<>();
        this.fsm_transitions = new ArrayList<>();
    }

    public FSM_StateMachine(
        ArrayList<FSM_State> fsm_states,        ArrayList<FSM_Transition> fsm_transitions    ) {
        this.fsm_states = fsm_states;
        this.fsm_transitions = fsm_transitions;
    }


    public FSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(FSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public List<FSM_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public FSM_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(FSM_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public List<FSM_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }

}