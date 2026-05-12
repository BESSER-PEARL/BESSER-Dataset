





import java.util.List;
import java.util.ArrayList;

public class states_CompoundState extends State {






    private states_Statemachine states_statemachine;


    public states_CompoundState(
    ) {
        super(
        );
    }



    public states_Statemachine getStates_statemachine() {
        return states_statemachine;
    }

    public void setStates_statemachine(states_Statemachine states_statemachine) {
        this.states_statemachine = states_statemachine;
    }

}