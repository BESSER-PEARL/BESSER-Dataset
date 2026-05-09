





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Command  {

    private String name;





    private stateMachine_StateMachine statemachine_statemachine;


    public stateMachine_Command(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}