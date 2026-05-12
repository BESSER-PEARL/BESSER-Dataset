





import java.util.List;
import java.util.ArrayList;

public class fsm_AbstractState extends NamedElement {






    private List<fsm_Transition> fsm_transitions;




    private List<fsm_Transition> fsm_transitions;




    private fsm_Transition fsm_transition;




    private fsm_Transition fsm_transition;


    public fsm_AbstractState(
    ) {
        super(
        );
        this.fsm_transitions = new ArrayList<>();
        this.fsm_transitions = new ArrayList<>();
    }

    public fsm_AbstractState(
        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_Transition> fsm_transitions    ) {
        this.fsm_transitions = fsm_transitions;
        this.fsm_transitions = fsm_transitions;
    }


    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}