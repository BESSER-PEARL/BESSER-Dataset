





import java.util.List;
import java.util.ArrayList;

public class fsm_State  {

    private String name;





    private fsm_Transition fsm_transition;




    private fsm_FSM fsm_fsm;




    private fsm_Transition fsm_transition;


    public fsm_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}