





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_CompositeState extends State {






    private SimplStateMachine_State simplstatemachine_state;




    private SimplStateMachine_InitialState simplstatemachine_initialstate;




    private List<SimplStateMachine_State> simplstatemachine_states;


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


    public SimplStateMachine_State getSimplstatemachine_state() {
        return simplstatemachine_state;
    }

    public void setSimplstatemachine_state(SimplStateMachine_State simplstatemachine_state) {
        this.simplstatemachine_state = simplstatemachine_state;
    }
    public SimplStateMachine_InitialState getSimplstatemachine_initialstate() {
        return simplstatemachine_initialstate;
    }

    public void setSimplstatemachine_initialstate(SimplStateMachine_InitialState simplstatemachine_initialstate) {
        this.simplstatemachine_initialstate = simplstatemachine_initialstate;
    }
    public List<SimplStateMachine_State> getSimplstatemachine_states() {
        return simplstatemachine_states;
    }

    public void addSimplstatemachine_state(Simplstatemachine_state simplstatemachine_state) {
        this.simplstatemachine_states.add(simplstatemachine_state);
    }

}