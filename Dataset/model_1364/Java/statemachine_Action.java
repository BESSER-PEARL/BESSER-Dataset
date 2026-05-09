





import java.util.List;
import java.util.ArrayList;

public class statemachine_Action  {

    private String actionLabel;
    private String actionStatement;



    public statemachine_Action(
        String actionLabel,        String actionStatement    ) {
        this.actionLabel = actionLabel;
        this.actionStatement = actionStatement;
    }


    public String getActionlabel() {
        return actionLabel;
    }

    public void setActionlabel(String actionLabel) {
        this.actionLabel = actionLabel;
    }
    public String getActionstatement() {
        return actionStatement;
    }

    public void setActionstatement(String actionStatement) {
        this.actionStatement = actionStatement;
    }


}