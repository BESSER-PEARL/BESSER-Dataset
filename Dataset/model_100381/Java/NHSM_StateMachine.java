





import java.util.List;
import java.util.ArrayList;

public class NHSM_StateMachine  {

    private String name;





    private NHSM_State nhsm_state;




    private List<NHSM_Transition> nhsm_transitions;




    private List<NHSM_State> nhsm_states;




    private NHSM_Transition nhsm_transition;


    public NHSM_StateMachine(
        String name    ) {
        this.name = name;
        this.nhsm_transitions = new ArrayList<>();
        this.nhsm_states = new ArrayList<>();
    }

    public NHSM_StateMachine(
        String name        ArrayList<NHSM_Transition> nhsm_transitions,        ArrayList<NHSM_State> nhsm_states    ) {
        this.name = name;
        this.nhsm_transitions = nhsm_transitions;
        this.nhsm_states = nhsm_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public NHSM_State getNhsm_state() {
        return nhsm_state;
    }

    public void setNhsm_state(NHSM_State nhsm_state) {
        this.nhsm_state = nhsm_state;
    }
    public List<NHSM_Transition> getNhsm_transitions() {
        return nhsm_transitions;
    }

    public void addNhsm_transition(Nhsm_transition nhsm_transition) {
        this.nhsm_transitions.add(nhsm_transition);
    }
    public List<NHSM_State> getNhsm_states() {
        return nhsm_states;
    }

    public void addNhsm_state(Nhsm_state nhsm_state) {
        this.nhsm_states.add(nhsm_state);
    }
    public NHSM_Transition getNhsm_transition() {
        return nhsm_transition;
    }

    public void setNhsm_transition(NHSM_Transition nhsm_transition) {
        this.nhsm_transition = nhsm_transition;
    }

}