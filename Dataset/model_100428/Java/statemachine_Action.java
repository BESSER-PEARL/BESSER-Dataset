





import java.util.List;
import java.util.ArrayList;

public class statemachine_Action  {

    private String actionLabel;





    private statemachine_Statement statemachine_statement;


    public statemachine_Action(
        String actionLabel    ) {
        this.actionLabel = actionLabel;
    }


    public String getActionlabel() {
        return actionLabel;
    }

    public void setActionlabel(String actionLabel) {
        this.actionLabel = actionLabel;
    }

    public statemachine_Statement getStatemachine_statement() {
        return statemachine_statement;
    }

    public void setStatemachine_statement(statemachine_Statement statemachine_statement) {
        this.statemachine_statement = statemachine_statement;
    }

}