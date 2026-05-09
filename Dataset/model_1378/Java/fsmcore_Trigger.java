





import java.util.List;
import java.util.ArrayList;

public class fsmcore_Trigger  {

    private String expression;





    private fsmcore_Transition fsmcore_transition;


    public fsmcore_Trigger(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public fsmcore_Transition getFsmcore_transition() {
        return fsmcore_transition;
    }

    public void setFsmcore_transition(fsmcore_Transition fsmcore_transition) {
        this.fsmcore_transition = fsmcore_transition;
    }

}