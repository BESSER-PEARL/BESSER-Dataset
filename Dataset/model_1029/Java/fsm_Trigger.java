





import java.util.List;
import java.util.ArrayList;

public class fsm_Trigger  {

    private String expression;





    private fsm_Transition fsm_transition;


    public fsm_Trigger(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}