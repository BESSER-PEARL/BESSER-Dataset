





import java.util.List;
import java.util.ArrayList;

public class fsa_State  {

    private boolean accepting;
    private String name;





    private fsa_Transition fsa_transition;




    private List<fsa_Transition> fsa_transitions;




    private List<fsa_Transition> fsa_transitions;




    private fsa_Transition fsa_transition;




    private fsa_FSA fsa_fsa;




    private fsa_FSA fsa_fsa;


    public fsa_State(
        boolean accepting,        String name    ) {
        this.accepting = accepting;
        this.name = name;
        this.fsa_transitions = new ArrayList<>();
        this.fsa_transitions = new ArrayList<>();
    }

    public fsa_State(
        boolean accepting,        String name        ArrayList<fsa_Transition> fsa_transitions,        ArrayList<fsa_Transition> fsa_transitions    ) {
        this.accepting = accepting;
        this.name = name;
        this.fsa_transitions = fsa_transitions;
        this.fsa_transitions = fsa_transitions;
    }

    public boolean getAccepting() {
        return accepting;
    }

    public void setAccepting(boolean accepting) {
        this.accepting = accepting;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsa_Transition getFsa_transition() {
        return fsa_transition;
    }

    public void setFsa_transition(fsa_Transition fsa_transition) {
        this.fsa_transition = fsa_transition;
    }
    public List<fsa_Transition> getFsa_transitions() {
        return fsa_transitions;
    }

    public void addFsa_transition(Fsa_transition fsa_transition) {
        this.fsa_transitions.add(fsa_transition);
    }
    public List<fsa_Transition> getFsa_transitions() {
        return fsa_transitions;
    }

    public void addFsa_transition(Fsa_transition fsa_transition) {
        this.fsa_transitions.add(fsa_transition);
    }
    public fsa_Transition getFsa_transition() {
        return fsa_transition;
    }

    public void setFsa_transition(fsa_Transition fsa_transition) {
        this.fsa_transition = fsa_transition;
    }
    public fsa_FSA getFsa_fsa() {
        return fsa_fsa;
    }

    public void setFsa_fsa(fsa_FSA fsa_fsa) {
        this.fsa_fsa = fsa_fsa;
    }
    public fsa_FSA getFsa_fsa() {
        return fsa_fsa;
    }

    public void setFsa_fsa(fsa_FSA fsa_fsa) {
        this.fsa_fsa = fsa_fsa;
    }

}