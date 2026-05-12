





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_State  {

    private boolean isActive;
    private String name;





    private SimplStateMachine_CompositeState simplstatemachine_compositestate;




    private SimplStateMachine_Transition simplstatemachine_transition;




    private SimplStateMachine_Transition simplstatemachine_transition;




    private SimplStateMachine_CompositeState simplstatemachine_compositestate;


    public SimplStateMachine_State(
        boolean isActive,        String name    ) {
        this.isActive = isActive;
        this.name = name;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimplStateMachine_CompositeState getSimplstatemachine_compositestate() {
        return simplstatemachine_compositestate;
    }

    public void setSimplstatemachine_compositestate(SimplStateMachine_CompositeState simplstatemachine_compositestate) {
        this.simplstatemachine_compositestate = simplstatemachine_compositestate;
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
    public SimplStateMachine_CompositeState getSimplstatemachine_compositestate() {
        return simplstatemachine_compositestate;
    }

    public void setSimplstatemachine_compositestate(SimplStateMachine_CompositeState simplstatemachine_compositestate) {
        this.simplstatemachine_compositestate = simplstatemachine_compositestate;
    }

}