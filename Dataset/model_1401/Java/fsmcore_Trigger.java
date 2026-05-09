





import java.util.List;
import java.util.ArrayList;

public class fsmcore_Trigger  {

    private boolean expression;





    private fsmcore_Transition fsmcore_transition;


    public fsmcore_Trigger(
        boolean expression    ) {
        this.expression = expression;
    }


    public boolean getExpression() {
        return expression;
    }

    public void setExpression(boolean expression) {
        this.expression = expression;
    }

    public fsmcore_Transition getFsmcore_transition() {
        return fsmcore_transition;
    }

    public void setFsmcore_transition(fsmcore_Transition fsmcore_transition) {
        this.fsmcore_transition = fsmcore_transition;
    }

}