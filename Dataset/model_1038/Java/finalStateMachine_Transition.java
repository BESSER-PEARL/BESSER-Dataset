





import java.util.List;
import java.util.ArrayList;

public class finalStateMachine_Transition  {

    private String name;





    private finalStateMachine_FSM finalstatemachine_fsm;


    public finalStateMachine_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public finalStateMachine_FSM getFinalstatemachine_fsm() {
        return finalstatemachine_fsm;
    }

    public void setFinalstatemachine_fsm(finalStateMachine_FSM finalstatemachine_fsm) {
        this.finalstatemachine_fsm = finalstatemachine_fsm;
    }

}