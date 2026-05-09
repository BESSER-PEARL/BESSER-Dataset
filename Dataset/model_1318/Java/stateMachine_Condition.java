





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Condition  {

    private String name;





    private stateMachine_Transition statemachine_transition;


    public stateMachine_Condition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(stateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }

}