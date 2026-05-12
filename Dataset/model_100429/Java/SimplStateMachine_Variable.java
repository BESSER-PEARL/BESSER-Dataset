





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_Variable  {

    private String name;





    private SimplStateMachine_StateMachine simplstatemachine_statemachine;


    public SimplStateMachine_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimplStateMachine_StateMachine getSimplstatemachine_statemachine() {
        return simplstatemachine_statemachine;
    }

    public void setSimplstatemachine_statemachine(SimplStateMachine_StateMachine simplstatemachine_statemachine) {
        this.simplstatemachine_statemachine = simplstatemachine_statemachine;
    }

}