





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberVariable extends Variable {

    private boolean value;
    private int initialValue;





    private fsm_Action fsm_action;




    private fsm_NumberGuard fsm_numberguard;


    public fsm_NumberVariable(
        boolean value,        int initialValue    ) {
        super(
        );
        this.value = value;
        this.initialValue = initialValue;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
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
    public fsm_NumberGuard getFsm_numberguard() {
        return fsm_numberguard;
    }

    public void setFsm_numberguard(fsm_NumberGuard fsm_numberguard) {
        this.fsm_numberguard = fsm_numberguard;
    }

}