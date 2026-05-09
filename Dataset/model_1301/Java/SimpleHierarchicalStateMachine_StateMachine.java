





import java.util.List;
import java.util.ArrayList;

public class SimpleHierarchicalStateMachine_StateMachine  {






    private List<SimpleHierarchicalStateMachine_Transition> simplehierarchicalstatemachine_transitions;




    private List<SimpleHierarchicalStateMachine_State> simplehierarchicalstatemachine_states;


    public SimpleHierarchicalStateMachine_StateMachine(
    ) {
        this.simplehierarchicalstatemachine_transitions = new ArrayList<>();
        this.simplehierarchicalstatemachine_states = new ArrayList<>();
    }

    public SimpleHierarchicalStateMachine_StateMachine(
        ArrayList<SimpleHierarchicalStateMachine_Transition> simplehierarchicalstatemachine_transitions,        ArrayList<SimpleHierarchicalStateMachine_State> simplehierarchicalstatemachine_states    ) {
        this.simplehierarchicalstatemachine_transitions = simplehierarchicalstatemachine_transitions;
        this.simplehierarchicalstatemachine_states = simplehierarchicalstatemachine_states;
    }


    public List<SimpleHierarchicalStateMachine_Transition> getSimplehierarchicalstatemachine_transitions() {
        return simplehierarchicalstatemachine_transitions;
    }

    public void addSimplehierarchicalstatemachine_transition(Simplehierarchicalstatemachine_transition simplehierarchicalstatemachine_transition) {
        this.simplehierarchicalstatemachine_transitions.add(simplehierarchicalstatemachine_transition);
    }
    public List<SimpleHierarchicalStateMachine_State> getSimplehierarchicalstatemachine_states() {
        return simplehierarchicalstatemachine_states;
    }

    public void addSimplehierarchicalstatemachine_state(Simplehierarchicalstatemachine_state simplehierarchicalstatemachine_state) {
        this.simplehierarchicalstatemachine_states.add(simplehierarchicalstatemachine_state);
    }

}