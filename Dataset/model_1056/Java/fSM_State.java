





import java.util.List;
import java.util.ArrayList;

public class fSM_State  {






    private List<fSM_Transition> fsm_transitions;




    private fSM_Transition fsm_transition;




    private fSM_FSM fsm_fsm;


    public fSM_State(
    ) {
        this.fsm_transitions = new ArrayList<>();
    }

    public fSM_State(
        ArrayList<fSM_Transition> fsm_transitions    ) {
        this.fsm_transitions = fsm_transitions;
    }


    public List<fSM_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public fSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fSM_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fSM_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }

}