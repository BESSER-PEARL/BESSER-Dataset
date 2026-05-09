





import java.util.List;
import java.util.ArrayList;

public class fsml_FSMTransition  {

    private String action;
    private String input;





    private fsml_FSMState fsml_fsmstate;




    private fsml_FSMState fsml_fsmstate;


    public fsml_FSMTransition(
        String action,        String input    ) {
        this.action = action;
        this.input = input;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }

    public fsml_FSMState getFsml_fsmstate() {
        return fsml_fsmstate;
    }

    public void setFsml_fsmstate(fsml_FSMState fsml_fsmstate) {
        this.fsml_fsmstate = fsml_fsmstate;
    }
    public fsml_FSMState getFsml_fsmstate() {
        return fsml_fsmstate;
    }

    public void setFsml_fsmstate(fsml_FSMState fsml_fsmstate) {
        this.fsml_fsmstate = fsml_fsmstate;
    }

}