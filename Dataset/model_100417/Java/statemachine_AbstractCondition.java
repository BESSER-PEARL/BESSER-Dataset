





import java.util.List;
import java.util.ArrayList;

public class statemachine_AbstractCondition  {

    private boolean isNotCondition;





    private statemachine_StateValue statemachine_statevalue;




    private statemachine_ConditionalState statemachine_conditionalstate;


    public statemachine_AbstractCondition(
        boolean isNotCondition    ) {
        this.isNotCondition = isNotCondition;
    }


    public boolean getIsnotcondition() {
        return isNotCondition;
    }

    public void setIsnotcondition(boolean isNotCondition) {
        this.isNotCondition = isNotCondition;
    }

    public statemachine_StateValue getStatemachine_statevalue() {
        return statemachine_statevalue;
    }

    public void setStatemachine_statevalue(statemachine_StateValue statemachine_statevalue) {
        this.statemachine_statevalue = statemachine_statevalue;
    }
    public statemachine_ConditionalState getStatemachine_conditionalstate() {
        return statemachine_conditionalstate;
    }

    public void setStatemachine_conditionalstate(statemachine_ConditionalState statemachine_conditionalstate) {
        this.statemachine_conditionalstate = statemachine_conditionalstate;
    }

}