





import java.util.List;
import java.util.ArrayList;

public class stateMachineEditRules_DFA  {






    private List<stateMachineEditRules_Transition> statemachineeditrules_transitions;




    private List<stateMachineEditRules_State> statemachineeditrules_states;


    public stateMachineEditRules_DFA(
    ) {
        this.statemachineeditrules_transitions = new ArrayList<>();
        this.statemachineeditrules_states = new ArrayList<>();
    }

    public stateMachineEditRules_DFA(
        ArrayList<stateMachineEditRules_Transition> statemachineeditrules_transitions,        ArrayList<stateMachineEditRules_State> statemachineeditrules_states    ) {
        this.statemachineeditrules_transitions = statemachineeditrules_transitions;
        this.statemachineeditrules_states = statemachineeditrules_states;
    }


    public List<stateMachineEditRules_Transition> getStatemachineeditrules_transitions() {
        return statemachineeditrules_transitions;
    }

    public void addStatemachineeditrules_transition(Statemachineeditrules_transition statemachineeditrules_transition) {
        this.statemachineeditrules_transitions.add(statemachineeditrules_transition);
    }
    public List<stateMachineEditRules_State> getStatemachineeditrules_states() {
        return statemachineeditrules_states;
    }

    public void addStatemachineeditrules_state(Statemachineeditrules_state statemachineeditrules_state) {
        this.statemachineeditrules_states.add(statemachineeditrules_state);
    }

}