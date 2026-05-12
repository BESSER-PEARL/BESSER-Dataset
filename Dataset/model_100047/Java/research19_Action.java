





import java.util.List;
import java.util.ArrayList;

public class research19_Action  {

    private String actionStatement;
    private String actionLabel;





    private research19_Action research19_action;




    private research19_State research19_state;




    private research19_Transition research19_transition;


    public research19_Action(
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

    public research19_Action getResearch19_action() {
        return research19_action;
    }

    public void setResearch19_action(research19_Action research19_action) {
        this.research19_action = research19_action;
    }
    public research19_State getResearch19_state() {
        return research19_state;
    }

    public void setResearch19_state(research19_State research19_state) {
        this.research19_state = research19_state;
    }
    public research19_Transition getResearch19_transition() {
        return research19_transition;
    }

    public void setResearch19_transition(research19_Transition research19_transition) {
        this.research19_transition = research19_transition;
    }

}