





import java.util.List;
import java.util.ArrayList;

public class statemachine_Call extends Value {

    private String actionId;





    private statemachine_CallAction statemachine_callaction;


    public statemachine_Call(
        String actionId    ) {
        super(
        );
        this.actionId = actionId;
    }


    public String getActionid() {
        return actionId;
    }

    public void setActionid(String actionId) {
        this.actionId = actionId;
    }

    public statemachine_CallAction getStatemachine_callaction() {
        return statemachine_callaction;
    }

    public void setStatemachine_callaction(statemachine_CallAction statemachine_callaction) {
        this.statemachine_callaction = statemachine_callaction;
    }

}