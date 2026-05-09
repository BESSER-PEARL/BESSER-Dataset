





import java.util.List;
import java.util.ArrayList;

public class stateMachine_StateMachine  {

    private String name;





    private stateMachine_Model statemachine_model;


    public stateMachine_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachine_Model getStatemachine_model() {
        return statemachine_model;
    }

    public void setStatemachine_model(stateMachine_Model statemachine_model) {
        this.statemachine_model = statemachine_model;
    }

}