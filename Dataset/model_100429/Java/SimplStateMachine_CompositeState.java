





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_CompositeState extends State {






    private List<SimplStateMachine_State> simplstatemachine_states;




    private SimplStateMachine_State simplstatemachine_state;


    public SimplStateMachine_CompositeState(
    ) {
        super(
        );
        this.simplstatemachine_states = new ArrayList<>();
    }

    public SimplStateMachine_CompositeState(
        ArrayList<SimplStateMachine_State> simplstatemachine_states    ) {
        this.simplstatemachine_states = simplstatemachine_states;
    }


    public List<SimplStateMachine_State> getSimplstatemachine_states() {
        return simplstatemachine_states;
    }

    public void addSimplstatemachine_state(Simplstatemachine_state simplstatemachine_state) {
        this.simplstatemachine_states.add(simplstatemachine_state);
    }
    public SimplStateMachine_State getSimplstatemachine_state() {
        return simplstatemachine_state;
    }

    public void setSimplstatemachine_state(SimplStateMachine_State simplstatemachine_state) {
        this.simplstatemachine_state = simplstatemachine_state;
    }

}