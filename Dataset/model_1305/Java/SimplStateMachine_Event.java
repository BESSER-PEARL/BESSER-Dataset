





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_Event  {

    private String name;





    private SimplStateMachine_Transition simplstatemachine_transition;




    private SimplStateMachine_StateMachine simplstatemachine_statemachine;


    public SimplStateMachine_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimplStateMachine_Transition getSimplstatemachine_transition() {
        return simplstatemachine_transition;
    }

    public void setSimplstatemachine_transition(SimplStateMachine_Transition simplstatemachine_transition) {
        this.simplstatemachine_transition = simplstatemachine_transition;
    }
    public SimplStateMachine_StateMachine getSimplstatemachine_statemachine() {
        return simplstatemachine_statemachine;
    }

    public void setSimplstatemachine_statemachine(SimplStateMachine_StateMachine simplstatemachine_statemachine) {
        this.simplstatemachine_statemachine = simplstatemachine_statemachine;
    }

}