





import java.util.List;
import java.util.ArrayList;

public class research16_Action  {

    private String actionLabel;
    private String actionStatement;





    private research16_Transition research16_transition;




    private research16_State research16_state;




    private research16_Action research16_action;


    public research16_Action(
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

    public research16_Transition getResearch16_transition() {
        return research16_transition;
    }

    public void setResearch16_transition(research16_Transition research16_transition) {
        this.research16_transition = research16_transition;
    }
    public research16_State getResearch16_state() {
        return research16_state;
    }

    public void setResearch16_state(research16_State research16_state) {
        this.research16_state = research16_state;
    }
    public research16_Action getResearch16_action() {
        return research16_action;
    }

    public void setResearch16_action(research16_Action research16_action) {
        this.research16_action = research16_action;
    }

}