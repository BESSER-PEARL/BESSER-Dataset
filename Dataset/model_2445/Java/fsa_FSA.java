





import java.util.List;
import java.util.ArrayList;

public class fsa_FSA  {






    private List<fsa_Transition> fsa_transitions;


    public fsa_FSA(
    ) {
        this.fsa_transitions = new ArrayList<>();
    }

    public fsa_FSA(
        ArrayList<fsa_Transition> fsa_transitions    ) {
        this.fsa_transitions = fsa_transitions;
    }


    public List<fsa_Transition> getFsa_transitions() {
        return fsa_transitions;
    }

    public void addFsa_transition(Fsa_transition fsa_transition) {
        this.fsa_transitions.add(fsa_transition);
    }

}