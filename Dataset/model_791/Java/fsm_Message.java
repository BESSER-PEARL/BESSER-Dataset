





import java.util.List;
import java.util.ArrayList;

public class fsm_Message  {

    private String name;





    private fsm_State fsm_state;




    private fsm_Event fsm_event;




    private fsm_FSM fsm_fsm;


    public fsm_Message(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_Event getFsm_event() {
        return fsm_event;
    }

    public void setFsm_event(fsm_Event fsm_event) {
        this.fsm_event = fsm_event;
    }
    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }

}