





import java.util.List;
import java.util.ArrayList;

public class states_Event  {

    private String name;





    private states_Statemachine states_statemachine;




    private states_Transition states_transition;


    public states_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public states_Statemachine getStates_statemachine() {
        return states_statemachine;
    }

    public void setStates_statemachine(states_Statemachine states_statemachine) {
        this.states_statemachine = states_statemachine;
    }
    public states_Transition getStates_transition() {
        return states_transition;
    }

    public void setStates_transition(states_Transition states_transition) {
        this.states_transition = states_transition;
    }

}