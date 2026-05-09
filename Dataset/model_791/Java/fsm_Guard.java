





import java.util.List;
import java.util.ArrayList;

public class fsm_Guard  {

    private String name;





    private fsm_FSM fsm_fsm;


    public fsm_Guard(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }

}