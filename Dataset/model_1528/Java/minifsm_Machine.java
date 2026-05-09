





import java.util.List;
import java.util.ArrayList;

public class minifsm_Machine  {






    private List<minifsm_State> minifsm_states;




    private List<minifsm_Transition> minifsm_transitions;


    public minifsm_Machine(
    ) {
        this.minifsm_states = new ArrayList<>();
        this.minifsm_transitions = new ArrayList<>();
    }

    public minifsm_Machine(
        ArrayList<minifsm_State> minifsm_states,        ArrayList<minifsm_Transition> minifsm_transitions    ) {
        this.minifsm_states = minifsm_states;
        this.minifsm_transitions = minifsm_transitions;
    }


    public List<minifsm_State> getMinifsm_states() {
        return minifsm_states;
    }

    public void addMinifsm_state(Minifsm_state minifsm_state) {
        this.minifsm_states.add(minifsm_state);
    }
    public List<minifsm_Transition> getMinifsm_transitions() {
        return minifsm_transitions;
    }

    public void addMinifsm_transition(Minifsm_transition minifsm_transition) {
        this.minifsm_transitions.add(minifsm_transition);
    }

}