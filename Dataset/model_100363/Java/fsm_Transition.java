





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String guard;
    private String action;





    private fsm_State fsm_state;




    private fsm_SuperState fsm_superstate;




    private fsm_SuperState fsm_superstate;




    private fsm_SuperState fsm_superstate;


    public fsm_Transition(
        String guard,        String action    ) {
        this.guard = guard;
        this.action = action;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_SuperState getFsm_superstate() {
        return fsm_superstate;
    }

    public void setFsm_superstate(fsm_SuperState fsm_superstate) {
        this.fsm_superstate = fsm_superstate;
    }
    public fsm_SuperState getFsm_superstate() {
        return fsm_superstate;
    }

    public void setFsm_superstate(fsm_SuperState fsm_superstate) {
        this.fsm_superstate = fsm_superstate;
    }
    public fsm_SuperState getFsm_superstate() {
        return fsm_superstate;
    }

    public void setFsm_superstate(fsm_SuperState fsm_superstate) {
        this.fsm_superstate = fsm_superstate;
    }

}