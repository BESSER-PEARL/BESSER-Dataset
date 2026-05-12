





import java.util.List;
import java.util.ArrayList;

public class statemachine_Action  {

    private String actionStatement;
    private String actionLabel;



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


}