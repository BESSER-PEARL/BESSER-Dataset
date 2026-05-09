





import java.util.List;
import java.util.ArrayList;

public class fsm_tp_FSM  {

    private String name;





    private fsm_tp_InitialState fsm_tp_initialstate;


    public fsm_tp_FSM(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_tp_InitialState getFsm_tp_initialstate() {
        return fsm_tp_initialstate;
    }

    public void setFsm_tp_initialstate(fsm_tp_InitialState fsm_tp_initialstate) {
        this.fsm_tp_initialstate = fsm_tp_initialstate;
    }

}