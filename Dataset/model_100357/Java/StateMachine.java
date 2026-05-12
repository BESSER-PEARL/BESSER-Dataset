





import java.util.List;
import java.util.ArrayList;

public class StateMachine  {






    private FSM_State fsm_state;




    private FSM_Transition fsm_transition;


    public StateMachine(
    ) {
    }



    public FSM_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(FSM_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public FSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(FSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}