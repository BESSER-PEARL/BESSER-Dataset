





import java.util.List;
import java.util.ArrayList;

public class finalStateMachine_State  {

    private String name;





    private finalStateMachine_Transition finalstatemachine_transition;




    private finalStateMachine_FSM finalstatemachine_fsm;




    private finalStateMachine_Transition finalstatemachine_transition;


    public finalStateMachine_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public finalStateMachine_Transition getFinalstatemachine_transition() {
        return finalstatemachine_transition;
    }

    public void setFinalstatemachine_transition(finalStateMachine_Transition finalstatemachine_transition) {
        this.finalstatemachine_transition = finalstatemachine_transition;
    }
    public finalStateMachine_FSM getFinalstatemachine_fsm() {
        return finalstatemachine_fsm;
    }

    public void setFinalstatemachine_fsm(finalStateMachine_FSM finalstatemachine_fsm) {
        this.finalstatemachine_fsm = finalstatemachine_fsm;
    }
    public finalStateMachine_Transition getFinalstatemachine_transition() {
        return finalstatemachine_transition;
    }

    public void setFinalstatemachine_transition(finalStateMachine_Transition finalstatemachine_transition) {
        this.finalstatemachine_transition = finalstatemachine_transition;
    }

}