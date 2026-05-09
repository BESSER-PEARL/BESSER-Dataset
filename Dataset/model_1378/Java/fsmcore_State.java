





import java.util.List;
import java.util.ArrayList;

public class fsmcore_State extends NamedElement {






    private List<fsmcore_Transition> fsmcore_transitions;




    private fsmcore_Transition fsmcore_transition;




    private fsmcore_Transition fsmcore_transition;




    private List<fsmcore_Transition> fsmcore_transitions;


    public fsmcore_State(
    ) {
        super(
        );
        this.fsmcore_transitions = new ArrayList<>();
        this.fsmcore_transitions = new ArrayList<>();
    }

    public fsmcore_State(
        ArrayList<fsmcore_Transition> fsmcore_transitions,        ArrayList<fsmcore_Transition> fsmcore_transitions    ) {
        this.fsmcore_transitions = fsmcore_transitions;
        this.fsmcore_transitions = fsmcore_transitions;
    }


    public List<fsmcore_Transition> getFsmcore_transitions() {
        return fsmcore_transitions;
    }

    public void addFsmcore_transition(Fsmcore_transition fsmcore_transition) {
        this.fsmcore_transitions.add(fsmcore_transition);
    }
    public fsmcore_Transition getFsmcore_transition() {
        return fsmcore_transition;
    }

    public void setFsmcore_transition(fsmcore_Transition fsmcore_transition) {
        this.fsmcore_transition = fsmcore_transition;
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