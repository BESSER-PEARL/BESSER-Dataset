





import java.util.List;
import java.util.ArrayList;

public class fsm_Action  {

    private boolean value;
    private String variable;





    private fsm_Transition fsm_transition;


    public fsm_Action(
        boolean value,        String variable    ) {
        this.value = value;
        this.variable = variable;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}