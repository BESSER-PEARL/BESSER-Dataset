





import java.util.List;
import java.util.ArrayList;

public class UHSM_UTransition extends Transition {






    private List<UHSM_Transition> uhsm_transitions;


    public UHSM_UTransition(
    ) {
        super(
        );
        this.uhsm_transitions = new ArrayList<>();
    }

    public UHSM_UTransition(
        ArrayList<UHSM_Transition> uhsm_transitions    ) {
        this.uhsm_transitions = uhsm_transitions;
    }


    public List<UHSM_Transition> getUhsm_transitions() {
        return uhsm_transitions;
    }

    public void addUhsm_transition(Uhsm_transition uhsm_transition) {
        this.uhsm_transitions.add(uhsm_transition);
    }

}