





import java.util.List;
import java.util.ArrayList;

public class state_Constraint  {






    private state_OpaqueExpression state_opaqueexpression;




    private state_Transition state_transition;


    public state_Constraint(
    ) {
    }



    public state_OpaqueExpression getState_opaqueexpression() {
        return state_opaqueexpression;
    }

    public void setState_opaqueexpression(state_OpaqueExpression state_opaqueexpression) {
        this.state_opaqueexpression = state_opaqueexpression;
    }
    public state_Transition getState_transition() {
        return state_transition;
    }

    public void setState_transition(state_Transition state_transition) {
        this.state_transition = state_transition;
    }

}