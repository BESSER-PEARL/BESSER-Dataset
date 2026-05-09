





import java.util.List;
import java.util.ArrayList;

public class states_State  {

    private String name;
    private boolean initial;





    private states_Statemachine states_statemachine;


    public states_State(
        String name,        boolean initial    ) {
        this.name = name;
        this.initial = initial;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public states_Statemachine getStates_statemachine() {
        return states_statemachine;
    }

    public void setStates_statemachine(states_Statemachine states_statemachine) {
        this.states_statemachine = states_statemachine;
    }

}