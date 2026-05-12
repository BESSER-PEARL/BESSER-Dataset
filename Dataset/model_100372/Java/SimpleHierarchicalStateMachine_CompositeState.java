





import java.util.List;
import java.util.ArrayList;

public class SimpleHierarchicalStateMachine_CompositeState extends State {






    private SimpleHierarchicalStateMachine_State simplehierarchicalstatemachine_state;




    private List<SimpleHierarchicalStateMachine_State> simplehierarchicalstatemachine_states;


    public SimpleHierarchicalStateMachine_CompositeState(
    ) {
        super(
        );
        this.simplehierarchicalstatemachine_states = new ArrayList<>();
    }

    public SimpleHierarchicalStateMachine_CompositeState(
        ArrayList<SimpleHierarchicalStateMachine_State> simplehierarchicalstatemachine_states    ) {
        this.simplehierarchicalstatemachine_states = simplehierarchicalstatemachine_states;
    }


    public SimpleHierarchicalStateMachine_State getSimplehierarchicalstatemachine_state() {
        return simplehierarchicalstatemachine_state;
    }

    public void setSimplehierarchicalstatemachine_state(SimpleHierarchicalStateMachine_State simplehierarchicalstatemachine_state) {
        this.simplehierarchicalstatemachine_state = simplehierarchicalstatemachine_state;
    }
    public List<SimpleHierarchicalStateMachine_State> getSimplehierarchicalstatemachine_states() {
        return simplehierarchicalstatemachine_states;
    }

    public void addSimplehierarchicalstatemachine_state(Simplehierarchicalstatemachine_state simplehierarchicalstatemachine_state) {
        this.simplehierarchicalstatemachine_states.add(simplehierarchicalstatemachine_state);
    }

}