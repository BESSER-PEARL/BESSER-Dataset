





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_State  {

    private String name;
    private boolean isActive;





    private SimplStateMachine_Transition simplstatemachine_transition;




    private SimplStateMachine_Transition simplstatemachine_transition;


    public SimplStateMachine_State(
        String name,        boolean isActive    ) {
        this.name = name;
        this.isActive = isActive;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public SimplStateMachine_Transition getSimplstatemachine_transition() {
        return simplstatemachine_transition;
    }

    public void setSimplstatemachine_transition(SimplStateMachine_Transition simplstatemachine_transition) {
        this.simplstatemachine_transition = simplstatemachine_transition;
    }
    public SimplStateMachine_Transition getSimplstatemachine_transition() {
        return simplstatemachine_transition;
    }

    public void setSimplstatemachine_transition(SimplStateMachine_Transition simplstatemachine_transition) {
        this.simplstatemachine_transition = simplstatemachine_transition;
    }

}