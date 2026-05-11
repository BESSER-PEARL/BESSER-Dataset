





import java.util.List;
import java.util.ArrayList;

public class autopl_HierarchicalState extends State {






    private List<autopl_State> autopl_states;




    private List<autopl_Transition> autopl_transitions;


    public autopl_HierarchicalState(
    ) {
        super(
        );
        this.autopl_states = new ArrayList<>();
        this.autopl_transitions = new ArrayList<>();
    }

    public autopl_HierarchicalState(
        ArrayList<autopl_State> autopl_states,        ArrayList<autopl_Transition> autopl_transitions    ) {
        this.autopl_states = autopl_states;
        this.autopl_transitions = autopl_transitions;
    }


    public List<autopl_State> getAutopl_states() {
        return autopl_states;
    }

    public void addAutopl_state(Autopl_state autopl_state) {
        this.autopl_states.add(autopl_state);
    }
    public List<autopl_Transition> getAutopl_transitions() {
        return autopl_transitions;
    }

    public void addAutopl_transition(Autopl_transition autopl_transition) {
        this.autopl_transitions.add(autopl_transition);
    }

}