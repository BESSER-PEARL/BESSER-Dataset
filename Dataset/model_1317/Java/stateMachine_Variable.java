





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Variable  {

    private String name;





    private stateMachine_Variables statemachine_variables;


    public stateMachine_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachine_Variables getStatemachine_variables() {
        return statemachine_variables;
    }

    public void setStatemachine_variables(stateMachine_Variables statemachine_variables) {
        this.statemachine_variables = statemachine_variables;
    }

}