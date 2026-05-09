





import java.util.List;
import java.util.ArrayList;

public class HSM_StateMachine  {

    private String name;





    private HSM_Transition hsm_transition;




    private List<HSM_Transition> hsm_transitions;


    public HSM_StateMachine(
        String name    ) {
        this.name = name;
        this.hsm_transitions = new ArrayList<>();
    }

    public HSM_StateMachine(
        String name        ArrayList<HSM_Transition> hsm_transitions    ) {
        this.name = name;
        this.hsm_transitions = hsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }
    public List<HSM_Transition> getHsm_transitions() {
        return hsm_transitions;
    }

    public void addHsm_transition(Hsm_transition hsm_transition) {
        this.hsm_transitions.add(hsm_transition);
    }

}