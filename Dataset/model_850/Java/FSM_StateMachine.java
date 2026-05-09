





import java.util.List;
import java.util.ArrayList;

public class FSM_StateMachine extends NamedElement {






    private FSM_State fsm_state;




    private FSM_FSMModel fsm_fsmmodel;




    private List<FSM_State> fsm_states;


    public FSM_StateMachine(
    ) {
        super(
        );
        this.fsm_states = new ArrayList<>();
    }

    public FSM_StateMachine(
        ArrayList<FSM_State> fsm_states    ) {
        this.fsm_states = fsm_states;
    }


    public FSM_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(FSM_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public FSM_FSMModel getFsm_fsmmodel() {
        return fsm_fsmmodel;
    }

    public void setFsm_fsmmodel(FSM_FSMModel fsm_fsmmodel) {
        this.fsm_fsmmodel = fsm_fsmmodel;
    }
    public List<FSM_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }

}