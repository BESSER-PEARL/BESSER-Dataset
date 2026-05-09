





import java.util.List;
import java.util.ArrayList;

public class fsm_tp_State  {

    private String name;
    private boolean isFinal;





    private fsm_tp_FSM fsm_tp_fsm;


    public fsm_tp_State(
        String name,        boolean isFinal    ) {
        this.name = name;
        this.isFinal = isFinal;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public fsm_tp_FSM getFsm_tp_fsm() {
        return fsm_tp_fsm;
    }

    public void setFsm_tp_fsm(fsm_tp_FSM fsm_tp_fsm) {
        this.fsm_tp_fsm = fsm_tp_fsm;
    }

}