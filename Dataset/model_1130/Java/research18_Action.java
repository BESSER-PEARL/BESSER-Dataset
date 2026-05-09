





import java.util.List;
import java.util.ArrayList;

public class research18_Action  {

    private String actionLabel;
    private String actionStatement;





    private research18_Action research18_action;




    private research18_State research18_state;


    public research18_Action(
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

    public research18_Action getResearch18_action() {
        return research18_action;
    }

    public void setResearch18_action(research18_Action research18_action) {
        this.research18_action = research18_action;
    }
    public research18_State getResearch18_state() {
        return research18_state;
    }

    public void setResearch18_state(research18_State research18_state) {
        this.research18_state = research18_state;
    }

}