





import java.util.List;
import java.util.ArrayList;

public class fsm_tp_Transition  {

    private String trigger;
    private String name;





    private fsm_tp_FSM fsm_tp_fsm;




    private fsm_tp_State fsm_tp_state;




    private fsm_tp_State fsm_tp_state;


    public fsm_tp_Transition(
        String trigger,        String name    ) {
        this.trigger = trigger;
        this.name = name;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_tp_FSM getFsm_tp_fsm() {
        return fsm_tp_fsm;
    }

    public void setFsm_tp_fsm(fsm_tp_FSM fsm_tp_fsm) {
        this.fsm_tp_fsm = fsm_tp_fsm;
    }
    public fsm_tp_State getFsm_tp_state() {
        return fsm_tp_state;
    }

    public void setFsm_tp_state(fsm_tp_State fsm_tp_state) {
        this.fsm_tp_state = fsm_tp_state;
    }
    public fsm_tp_State getFsm_tp_state() {
        return fsm_tp_state;
    }

    public void setFsm_tp_state(fsm_tp_State fsm_tp_state) {
        this.fsm_tp_state = fsm_tp_state;
    }

}