





import java.util.List;
import java.util.ArrayList;

public class FSM_State extends NamedElement {

    private boolean isFinal;





    private FSM_Transition fsm_transition;




    private FSM_Transition fsm_transition;




    private List<FSM_Transition> fsm_transitions;


    public FSM_State(
        boolean isFinal    ) {
        super(
        );
        this.isFinal = isFinal;
        this.fsm_transitions = new ArrayList<>();
    }

    public FSM_State(
        boolean isFinal        ArrayList<FSM_Transition> fsm_transitions    ) {
        this.isFinal = isFinal;
        this.fsm_transitions = fsm_transitions;
    }

    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public FSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(FSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public FSM_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(FSM_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public List<FSM_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }

}