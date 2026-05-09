





import java.util.List;
import java.util.ArrayList;

public class statemachine103_Action  {

    private String actionLabel;
    private String actionStatement;





    private statemachine103_Action statemachine103_action;




    private statemachine103_NormalState statemachine103_normalstate;




    private statemachine103_Transition statemachine103_transition;


    public statemachine103_Action(
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

    public statemachine103_Action getStatemachine103_action() {
        return statemachine103_action;
    }

    public void setStatemachine103_action(statemachine103_Action statemachine103_action) {
        this.statemachine103_action = statemachine103_action;
    }
    public statemachine103_NormalState getStatemachine103_normalstate() {
        return statemachine103_normalstate;
    }

    public void setStatemachine103_normalstate(statemachine103_NormalState statemachine103_normalstate) {
        this.statemachine103_normalstate = statemachine103_normalstate;
    }
    public statemachine103_Transition getStatemachine103_transition() {
        return statemachine103_transition;
    }

    public void setStatemachine103_transition(statemachine103_Transition statemachine103_transition) {
        this.statemachine103_transition = statemachine103_transition;
    }

}