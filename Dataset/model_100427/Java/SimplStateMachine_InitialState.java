





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_InitialState  {






    private SimplStateMachine_State simplstatemachine_state;




    private SimplStateMachine_CompositeState simplstatemachine_compositestate;


    public SimplStateMachine_InitialState(
    ) {
    }



    public SimplStateMachine_State getSimplstatemachine_state() {
        return simplstatemachine_state;
    }

    public void setSimplstatemachine_state(SimplStateMachine_State simplstatemachine_state) {
        this.simplstatemachine_state = simplstatemachine_state;
    }
    public SimplStateMachine_CompositeState getSimplstatemachine_compositestate() {
        return simplstatemachine_compositestate;
    }

    public void setSimplstatemachine_compositestate(SimplStateMachine_CompositeState simplstatemachine_compositestate) {
        this.simplstatemachine_compositestate = simplstatemachine_compositestate;
    }

}