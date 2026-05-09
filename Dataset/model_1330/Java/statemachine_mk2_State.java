





import java.util.List;
import java.util.ArrayList;

public class statemachine_mk2_State  {

    private String name;





    private statemachine_mk2_StateMachine statemachine_mk2_statemachine;


    public statemachine_mk2_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_mk2_StateMachine getStatemachine_mk2_statemachine() {
        return statemachine_mk2_statemachine;
    }

    public void setStatemachine_mk2_statemachine(statemachine_mk2_StateMachine statemachine_mk2_statemachine) {
        this.statemachine_mk2_statemachine = statemachine_mk2_statemachine;
    }

}