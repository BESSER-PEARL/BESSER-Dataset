





import java.util.List;
import java.util.ArrayList;

public class fsm_eAction  {

    private String exitLabel;





    private fsm_State fsm_state;


    public fsm_eAction(
        String exitLabel    ) {
        this.exitLabel = exitLabel;
    }


    public String getExitlabel() {
        return exitLabel;
    }

    public void setExitlabel(String exitLabel) {
        this.exitLabel = exitLabel;
    }

    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}