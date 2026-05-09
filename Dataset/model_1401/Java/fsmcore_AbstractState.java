





import java.util.List;
import java.util.ArrayList;

public class fsmcore_AbstractState extends NamedElement {






    private fsmcore_Transition fsmcore_transition;




    private List<fsmcore_Transition> fsmcore_transitions;




    private fsmcore_Region fsmcore_region;




    private fsmcore_Region fsmcore_region;




    private fsmcore_Transition fsmcore_transition;




    private List<fsmcore_Transition> fsmcore_transitions;


    public fsmcore_AbstractState(
    ) {
        super(
        );
        this.fsmcore_transitions = new ArrayList<>();
        this.fsmcore_transitions = new ArrayList<>();
    }

    public fsmcore_AbstractState(
        ArrayList<fsmcore_Transition> fsmcore_transitions,        ArrayList<fsmcore_Transition> fsmcore_transitions    ) {
        this.fsmcore_transitions = fsmcore_transitions;
        this.fsmcore_transitions = fsmcore_transitions;
    }


    public fsmcore_Transition getFsmcore_transition() {
        return fsmcore_transition;
    }

    public void setFsmcore_transition(fsmcore_Transition fsmcore_transition) {
        this.fsmcore_transition = fsmcore_transition;
    }
    public List<fsmcore_Transition> getFsmcore_transitions() {
        return fsmcore_transitions;
    }

    public void addFsmcore_transition(Fsmcore_transition fsmcore_transition) {
        this.fsmcore_transitions.add(fsmcore_transition);
    }
    public fsmcore_Region getFsmcore_region() {
        return fsmcore_region;
    }

    public void setFsmcore_region(fsmcore_Region fsmcore_region) {
        this.fsmcore_region = fsmcore_region;
    }
    public fsmcore_Region getFsmcore_region() {
        return fsmcore_region;
    }

    public void setFsmcore_region(fsmcore_Region fsmcore_region) {
        this.fsmcore_region = fsmcore_region;
    }
    public fsmcore_Transition getFsmcore_transition() {
        return fsmcore_transition;
    }

    public void setFsmcore_transition(fsmcore_Transition fsmcore_transition) {
        this.fsmcore_transition = fsmcore_transition;
    }
    public List<fsmcore_Transition> getFsmcore_transitions() {
        return fsmcore_transitions;
    }

    public void addFsmcore_transition(Fsmcore_transition fsmcore_transition) {
        this.fsmcore_transitions.add(fsmcore_transition);
    }

}