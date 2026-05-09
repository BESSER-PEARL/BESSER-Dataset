





import java.util.List;
import java.util.ArrayList;

public class fsm_State  {

    private String name;
    private boolean initial;
    private boolean final;





    private fsm_FSM fsm_fsm;




    private fsm_FSM fsm_fsm;


    public fsm_State(
        String name,        boolean initial,        boolean final    ) {
        this.name = name;
        this.initial = initial;
        this.final = final;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }
    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }

}