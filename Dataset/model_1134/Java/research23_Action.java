





import java.util.List;
import java.util.ArrayList;

public class research23_Action  {

    private String actionStatement;
    private String actionLabel;





    private research23_Action research23_action;




    private research23_State research23_state;




    private research23_Transition research23_transition;


    public research23_Action(
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

    public research23_Action getResearch23_action() {
        return research23_action;
    }

    public void setResearch23_action(research23_Action research23_action) {
        this.research23_action = research23_action;
    }
    public research23_State getResearch23_state() {
        return research23_state;
    }

    public void setResearch23_state(research23_State research23_state) {
        this.research23_state = research23_state;
    }
    public research23_Transition getResearch23_transition() {
        return research23_transition;
    }

    public void setResearch23_transition(research23_Transition research23_transition) {
        this.research23_transition = research23_transition;
    }

}