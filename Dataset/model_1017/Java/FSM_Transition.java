





import java.util.List;
import java.util.ArrayList;

public class FSM_Transition  {

    private String label;
    private String genBy;





    private FSM_StateMachine fsm_statemachine;




    private FSM_StateMachine fsm_statemachine;


    public FSM_Transition(
        String label,        String genBy    ) {
        this.label = label;
        this.genBy = genBy;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getGenby() {
        return genBy;
    }

    public void setGenby(String genBy) {
        this.genBy = genBy;
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

}