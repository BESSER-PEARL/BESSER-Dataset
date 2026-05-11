





import java.util.List;
import java.util.ArrayList;

public class sAAP_StateMachine  {

    private String name;





    private List<sAAP_State> saap_states;




    private List<sAAP_Transition> saap_transitions;


    public sAAP_StateMachine(
        String name    ) {
        this.name = name;
        this.saap_states = new ArrayList<>();
        this.saap_transitions = new ArrayList<>();
    }

    public sAAP_StateMachine(
        String name        ArrayList<sAAP_State> saap_states,        ArrayList<sAAP_Transition> saap_transitions    ) {
        this.name = name;
        this.saap_states = saap_states;
        this.saap_transitions = saap_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sAAP_State> getSaap_states() {
        return saap_states;
    }

    public void addSaap_state(Saap_state saap_state) {
        this.saap_states.add(saap_state);
    }
    public List<sAAP_Transition> getSaap_transitions() {
        return saap_transitions;
    }

    public void addSaap_transition(Saap_transition saap_transition) {
        this.saap_transitions.add(saap_transition);
    }

}