





import java.util.List;
import java.util.ArrayList;

public class fsml_FSMState  {

    private boolean initial;
    private String name;





    private fsml_FSM fsml_fsm;


    public fsml_FSMState(
        boolean initial,        String name    ) {
        this.initial = initial;
        this.name = name;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsml_FSM getFsml_fsm() {
        return fsml_fsm;
    }

    public void setFsml_fsm(fsml_FSM fsml_fsm) {
        this.fsml_fsm = fsml_fsm;
    }

}