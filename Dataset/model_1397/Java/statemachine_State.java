





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String name;





    private List<statemachine_State> statemachine_states;




    private statemachine_Statemachine statemachine_statemachine;


    public statemachine_State(
        String name    ) {
        this.name = name;
        this.statemachine_states = new ArrayList<>();
    }

    public statemachine_State(
        String name        ArrayList<statemachine_State> statemachine_states    ) {
        this.name = name;
        this.statemachine_states = statemachine_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }
    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}