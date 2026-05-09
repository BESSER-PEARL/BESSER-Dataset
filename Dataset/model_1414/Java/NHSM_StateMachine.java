





import java.util.List;
import java.util.ArrayList;

public class NHSM_StateMachine  {






    private List<NHSM_Transition> nhsm_transitions;


    public NHSM_StateMachine(
    ) {
        this.nhsm_transitions = new ArrayList<>();
    }

    public NHSM_StateMachine(
        ArrayList<NHSM_Transition> nhsm_transitions    ) {
        this.nhsm_transitions = nhsm_transitions;
    }


    public List<NHSM_Transition> getNhsm_transitions() {
        return nhsm_transitions;
    }

    public void addNhsm_transition(Nhsm_transition nhsm_transition) {
        this.nhsm_transitions.add(nhsm_transition);
    }

}