





import java.util.List;
import java.util.ArrayList;

public class research20_Action  {

    private String actionLabel;
    private String actionStatement;





    private research20_State research20_state;




    private research20_Action research20_action;


    public research20_Action(
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

    public research20_State getResearch20_state() {
        return research20_state;
    }

    public void setResearch20_state(research20_State research20_state) {
        this.research20_state = research20_state;
    }
    public research20_Action getResearch20_action() {
        return research20_action;
    }

    public void setResearch20_action(research20_Action research20_action) {
        this.research20_action = research20_action;
    }

}