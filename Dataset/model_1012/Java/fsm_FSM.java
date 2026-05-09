





import java.util.List;
import java.util.ArrayList;

public class fsm_FSM  {

    private String name;





    private fsm_InitialState fsm_initialstate;


    public fsm_FSM(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_InitialState getFsm_initialstate() {
        return fsm_initialstate;
    }

    public void setFsm_initialstate(fsm_InitialState fsm_initialstate) {
        this.fsm_initialstate = fsm_initialstate;
    }

}