





import java.util.List;
import java.util.ArrayList;

public class HSM_StateMachine  {

    private String name;





    private List<HSM_Transition> hsm_transitions;




    private HSM_Transition hsm_transition;




    private HSM_AbstractState hsm_abstractstate;




    private List<HSM_AbstractState> hsm_abstractstates;


    public HSM_StateMachine(
        String name    ) {
        this.name = name;
        this.hsm_transitions = new ArrayList<>();
        this.hsm_abstractstates = new ArrayList<>();
    }

    public HSM_StateMachine(
        String name        ArrayList<HSM_Transition> hsm_transitions,        ArrayList<HSM_AbstractState> hsm_abstractstates    ) {
        this.name = name;
        this.hsm_transitions = hsm_transitions;
        this.hsm_abstractstates = hsm_abstractstates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public HSM_AbstractState getHsm_abstractstate() {
        return hsm_abstractstate;
    }

    public void setHsm_abstractstate(HSM_AbstractState hsm_abstractstate) {
        this.hsm_abstractstate = hsm_abstractstate;
    }
    public List<HSM_AbstractState> getHsm_abstractstates() {
        return hsm_abstractstates;
    }

    public void addHsm_abstractstate(Hsm_abstractstate hsm_abstractstate) {
        this.hsm_abstractstates.add(hsm_abstractstate);
    }

}