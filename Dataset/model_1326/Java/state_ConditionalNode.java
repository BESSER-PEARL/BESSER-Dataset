





import java.util.List;
import java.util.ArrayList;

public class state_ConditionalNode extends Node {






    private state_Condition state_condition;


    public state_ConditionalNode(
    ) {
        super(
        );
    }



    public state_Condition getState_condition() {
        return state_condition;
    }

    public void setState_condition(state_Condition state_condition) {
        this.state_condition = state_condition;
    }

}