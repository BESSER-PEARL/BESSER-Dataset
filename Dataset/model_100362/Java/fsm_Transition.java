





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String Effect;
    private String Guard;





    private fsm_State fsm_state;




    private fsm_SuperState fsm_superstate;




    private fsm_SuperState fsm_superstate;




    private fsm_SuperState fsm_superstate;


    public fsm_Transition(
        String Effect,        String Guard    ) {
        this.Effect = Effect;
        this.Guard = Guard;
    }


    public String getEffect() {
        return Effect;
    }

    public void setEffect(String Effect) {
        this.Effect = Effect;
    }
    public String getGuard() {
        return Guard;
    }

    public void setGuard(String Guard) {
        this.Guard = Guard;
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