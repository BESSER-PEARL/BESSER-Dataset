





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_StateMachine  {

    private String name;





    private stateMachineDsl_State statemachinedsl_state;




    private List<stateMachineDsl_State> statemachinedsl_states;


    public stateMachineDsl_StateMachine(
        String name    ) {
        this.name = name;
        this.statemachinedsl_states = new ArrayList<>();
    }

    public stateMachineDsl_StateMachine(
        String name        ArrayList<stateMachineDsl_State> statemachinedsl_states    ) {
        this.name = name;
        this.statemachinedsl_states = statemachinedsl_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachineDsl_State getStatemachinedsl_state() {
        return statemachinedsl_state;
    }

    public void setStatemachinedsl_state(stateMachineDsl_State statemachinedsl_state) {
        this.statemachinedsl_state = statemachinedsl_state;
    }
    public List<stateMachineDsl_State> getStatemachinedsl_states() {
        return statemachinedsl_states;
    }

    public void addStatemachinedsl_state(Statemachinedsl_state statemachinedsl_state) {
        this.statemachinedsl_states.add(statemachinedsl_state);
    }

}