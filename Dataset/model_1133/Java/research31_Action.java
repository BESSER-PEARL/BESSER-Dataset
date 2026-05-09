





import java.util.List;
import java.util.ArrayList;

public class research31_Action  {

    private String actionStatement;
    private String actionLabel;





    private research31_Transition research31_transition;




    private research31_State research31_state;




    private research31_Action research31_action;


    public research31_Action(
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

    public research31_Transition getResearch31_transition() {
        return research31_transition;
    }

    public void setResearch31_transition(research31_Transition research31_transition) {
        this.research31_transition = research31_transition;
    }
    public research31_State getResearch31_state() {
        return research31_state;
    }

    public void setResearch31_state(research31_State research31_state) {
        this.research31_state = research31_state;
    }
    public research31_Action getResearch31_action() {
        return research31_action;
    }

    public void setResearch31_action(research31_Action research31_action) {
        this.research31_action = research31_action;
    }

}