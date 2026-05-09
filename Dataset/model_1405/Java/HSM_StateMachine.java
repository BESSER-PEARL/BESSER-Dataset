





import java.util.List;
import java.util.ArrayList;

public class HSM_StateMachine  {

    private String name;





    private List<HSM_State> hsm_states;




    private HSM_State hsm_state;




    private List<HSM_Transition> hsm_transitions;




    private HSM_Transition hsm_transition;


    public HSM_StateMachine(
        String name    ) {
        this.name = name;
        this.hsm_states = new ArrayList<>();
        this.hsm_transitions = new ArrayList<>();
    }

    public HSM_StateMachine(
        String name        ArrayList<HSM_State> hsm_states,        ArrayList<HSM_Transition> hsm_transitions    ) {
        this.name = name;
        this.hsm_states = hsm_states;
        this.hsm_transitions = hsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<HSM_State> getHsm_states() {
        return hsm_states;
    }

    public void addHsm_state(Hsm_state hsm_state) {
        this.hsm_states.add(hsm_state);
    }
    public HSM_State getHsm_state() {
        return hsm_state;
    }

    public void setHsm_state(HSM_State hsm_state) {
        this.hsm_state = hsm_state;
    }
    public List<HSM_Transition> getHsm_transitions() {
        return hsm_transitions;
    }

    public void addHsm_transition(Hsm_transition hsm_transition) {
        this.hsm_transitions.add(hsm_transition);
    }
    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }

}