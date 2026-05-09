





import java.util.List;
import java.util.ArrayList;

public class fsm_AbstractState extends NamedElement {






    private fsm_Transition fsm_transition;




    private fsm_Region fsm_region;




    private fsm_Transition fsm_transition;




    private List<fsm_Transition> fsm_transitions;




    private fsm_Region fsm_region;




    private List<fsm_Transition> fsm_transitions;


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


    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_Region getFsm_region() {
        return fsm_region;
    }

    public void setFsm_region(fsm_Region fsm_region) {
        this.fsm_region = fsm_region;
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public fsm_Region getFsm_region() {
        return fsm_region;
    }

    public void setFsm_region(fsm_Region fsm_region) {
        this.fsm_region = fsm_region;
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }

}