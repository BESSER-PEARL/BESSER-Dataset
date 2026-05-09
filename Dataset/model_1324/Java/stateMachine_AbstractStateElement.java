





import java.util.List;
import java.util.ArrayList;

public class stateMachine_AbstractStateElement extends AbstractMachineElement {

    private String name;





    private stateMachine_StateTransition statemachine_statetransition;




    private stateMachine_StateTransition statemachine_statetransition;


    public stateMachine_AbstractStateElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachine_StateTransition getStatemachine_statetransition() {
        return statemachine_statetransition;
    }

    public void setStatemachine_statetransition(stateMachine_StateTransition statemachine_statetransition) {
        this.statemachine_statetransition = statemachine_statetransition;
    }
    public stateMachine_StateTransition getStatemachine_statetransition() {
        return statemachine_statetransition;
    }

    public void setStatemachine_statetransition(stateMachine_StateTransition statemachine_statetransition) {
        this.statemachine_statetransition = statemachine_statetransition;
    }

}