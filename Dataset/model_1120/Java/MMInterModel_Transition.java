





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_Transition extends Element {

    private String stateMachine;
    private String action;



    public MMInterModel_Transition(
        String stateMachine,        String action    ) {
        super(
        );
        this.stateMachine = stateMachine;
        this.action = action;
    }


    public String getStatemachine() {
        return stateMachine;
    }

    public void setStatemachine(String stateMachine) {
        this.stateMachine = stateMachine;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}