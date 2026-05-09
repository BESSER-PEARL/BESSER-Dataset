





import java.util.List;
import java.util.ArrayList;

public class fsm_Region extends NamedElement {






    private fsm_State fsm_state;




    private fsm_StateMachine fsm_statemachine;




    private List<fsm_Transition> fsm_transitions;




    private fsm_State fsm_state;


    public fsm_Region(
    ) {
        super(
        );
        this.fsm_transitions = new ArrayList<>();
    }

    public fsm_Region(
        ArrayList<fsm_Transition> fsm_transitions    ) {
        this.fsm_transitions = fsm_transitions;
    }


    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(fsm_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}