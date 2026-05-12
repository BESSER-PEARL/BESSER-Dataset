





import java.util.List;
import java.util.ArrayList;

public class research32_Action  {

    private String actionLabel;
    private String actionStatement;





    private research32_Transition research32_transition;




    private research32_Action research32_action;




    private research32_State research32_state;


    public research32_Action(
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

    public research32_Transition getResearch32_transition() {
        return research32_transition;
    }

    public void setResearch32_transition(research32_Transition research32_transition) {
        this.research32_transition = research32_transition;
    }
    public research32_Action getResearch32_action() {
        return research32_action;
    }

    public void setResearch32_action(research32_Action research32_action) {
        this.research32_action = research32_action;
    }
    public research32_State getResearch32_state() {
        return research32_state;
    }

    public void setResearch32_state(research32_State research32_state) {
        this.research32_state = research32_state;
    }

}