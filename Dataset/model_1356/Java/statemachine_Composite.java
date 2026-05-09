





import java.util.List;
import java.util.ArrayList;

public class statemachine_Composite extends State {






    private List<statemachine_State> statemachine_states;


    public statemachine_Composite(
    ) {
        super(
        );
        this.statemachine_states = new ArrayList<>();
    }

    public statemachine_Composite(
        ArrayList<statemachine_State> statemachine_states    ) {
        this.statemachine_states = statemachine_states;
    }


    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }

}