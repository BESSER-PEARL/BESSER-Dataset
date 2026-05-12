





import java.util.List;
import java.util.ArrayList;

public class state_Condition  {

    private String expression;





    private state_ConditionalNode state_conditionalnode;




    private state_Transition state_transition;


    public state_Condition(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public state_ConditionalNode getState_conditionalnode() {
        return state_conditionalnode;
    }

    public void setState_conditionalnode(state_ConditionalNode state_conditionalnode) {
        this.state_conditionalnode = state_conditionalnode;
    }
    public state_Transition getState_transition() {
        return state_transition;
    }

    public void setState_transition(state_Transition state_transition) {
        this.state_transition = state_transition;
    }

}