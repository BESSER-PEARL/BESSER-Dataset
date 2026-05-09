





import java.util.List;
import java.util.ArrayList;

public class statemachines_State  {

    private String name;





    private statemachines_StateMachine statemachines_statemachine;


    public statemachines_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachines_StateMachine getStatemachines_statemachine() {
        return statemachines_statemachine;
    }

    public void setStatemachines_statemachine(statemachines_StateMachine statemachines_statemachine) {
        this.statemachines_statemachine = statemachines_statemachine;
    }

}