





import java.util.List;
import java.util.ArrayList;

public class statemachine_Action  {

    private String actionStatement;
    private String actionLabel;





    private statemachine_NormalState statemachine_normalstate;


    public statemachine_Action(
        String actionStatement,        String actionLabel    ) {
        this.actionStatement = actionStatement;
        this.actionLabel = actionLabel;
    }


    public String getActionstatement() {
        return actionStatement;
    }

    public void setActionstatement(String actionStatement) {
        this.actionStatement = actionStatement;
    }
    public String getActionlabel() {
        return actionLabel;
    }

    public void setActionlabel(String actionLabel) {
        this.actionLabel = actionLabel;
    }

    public statemachine_NormalState getStatemachine_normalstate() {
        return statemachine_normalstate;
    }

    public void setStatemachine_normalstate(statemachine_NormalState statemachine_normalstate) {
        this.statemachine_normalstate = statemachine_normalstate;
    }

}