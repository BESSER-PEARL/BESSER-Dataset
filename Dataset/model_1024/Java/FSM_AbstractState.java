





import java.util.List;
import java.util.ArrayList;

public class FSM_AbstractState  {

    private String name;





    private FSM_Transition fsm_transition;




    private FSM_StateMachine fsm_statemachine;




    private FSM_StateMachine fsm_statemachine;




    private FSM_CompositeState fsm_compositestate;




    private FSM_Transition fsm_transition;




    private FSM_CompositeState fsm_compositestate;


    public FSM_AbstractState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(FSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public FSM_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(FSM_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public FSM_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(FSM_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public FSM_CompositeState getFsm_compositestate() {
        return fsm_compositestate;
    }

    public void setFsm_compositestate(FSM_CompositeState fsm_compositestate) {
        this.fsm_compositestate = fsm_compositestate;
    }
    public FSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(FSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public FSM_CompositeState getFsm_compositestate() {
        return fsm_compositestate;
    }

    public void setFsm_compositestate(FSM_CompositeState fsm_compositestate) {
        this.fsm_compositestate = fsm_compositestate;
    }

}