





import java.util.List;
import java.util.ArrayList;

public class fsm_Action  {

    private String variable;
    private boolean value;





    private fsm_Transition fsm_transition;


    public fsm_Action(
        String variable,        boolean value    ) {
        this.variable = variable;
        this.value = value;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}