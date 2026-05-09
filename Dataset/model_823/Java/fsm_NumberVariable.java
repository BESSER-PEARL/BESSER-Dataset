





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberVariable extends Variable {

    private int initialValue;





    private fsm_Action fsm_action;


    public fsm_NumberVariable(
        int initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public int getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(int initialValue) {
        this.initialValue = initialValue;
    }

    public fsm_Action getFsm_action() {
        return fsm_action;
    }

    public void setFsm_action(fsm_Action fsm_action) {
        this.fsm_action = fsm_action;
    }

}