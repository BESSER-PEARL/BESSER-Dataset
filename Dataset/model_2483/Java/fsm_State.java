





import java.util.List;
import java.util.ArrayList;

public class fsm_State  {






    private List<fsm_Transition> fsm_transitions;




    private List<fsm_State> fsm_states;




    private List<fsm_FSM> fsm_fsms;


    public fsm_State(
    ) {
        this.fsm_transitions = new ArrayList<>();
        this.fsm_states = new ArrayList<>();
        this.fsm_fsms = new ArrayList<>();
    }

    public fsm_State(
        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_State> fsm_states,        ArrayList<fsm_FSM> fsm_fsms    ) {
        this.fsm_transitions = fsm_transitions;
        this.fsm_states = fsm_states;
        this.fsm_fsms = fsm_fsms;
    }


    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public List<fsm_FSM> getFsm_fsms() {
        return fsm_fsms;
    }

    public void addFsm_fsm(Fsm_fsm fsm_fsm) {
        this.fsm_fsms.add(fsm_fsm);
    }

}