





import java.util.List;
import java.util.ArrayList;

public class states_State  {

    private boolean initial;
    private String name;





    private states_Statemachine states_statemachine;


    public states_State(
        boolean initial,        String name    ) {
        this.initial = initial;
        this.name = name;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
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

}