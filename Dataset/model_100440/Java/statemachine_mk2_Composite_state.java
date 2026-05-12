





import java.util.List;
import java.util.ArrayList;

public class statemachine_mk2_Composite_state extends State {






    private List<statemachine_mk2_State> statemachine_mk2_states;




    private statemachine_mk2_StateMachine statemachine_mk2_statemachine;


    public statemachine_mk2_Composite_state(
    ) {
        super(
        );
        this.statemachine_mk2_states = new ArrayList<>();
    }

    public statemachine_mk2_Composite_state(
        ArrayList<statemachine_mk2_State> statemachine_mk2_states    ) {
        this.statemachine_mk2_states = statemachine_mk2_states;
    }


    public List<statemachine_mk2_State> getStatemachine_mk2_states() {
        return statemachine_mk2_states;
    }

    public void addStatemachine_mk2_state(Statemachine_mk2_state statemachine_mk2_state) {
        this.statemachine_mk2_states.add(statemachine_mk2_state);
    }
    public statemachine_mk2_StateMachine getStatemachine_mk2_statemachine() {
        return statemachine_mk2_statemachine;
    }

    public void setStatemachine_mk2_statemachine(statemachine_mk2_StateMachine statemachine_mk2_statemachine) {
        this.statemachine_mk2_statemachine = statemachine_mk2_statemachine;
    }

}