





import java.util.List;
import java.util.ArrayList;

public class research18_Transition extends StateMachineObject {

    private String guardLabel;
    private String guardExpression;





    private research18_State research18_state;




    private research18_State research18_state;




    private research18_State research18_state;




    private List<research18_Action> research18_actions;


    public research18_Transition(
        String guardLabel,        String guardExpression    ) {
        super(
        );
        this.guardLabel = guardLabel;
        this.guardExpression = guardExpression;
        this.research18_actions = new ArrayList<>();
    }

    public research18_Transition(
        String guardLabel,        String guardExpression        ArrayList<research18_Action> research18_actions    ) {
        this.guardLabel = guardLabel;
        this.guardExpression = guardExpression;
        this.research18_actions = research18_actions;
    }

    public String getGuardlabel() {
        return guardLabel;
    }

    public void setGuardlabel(String guardLabel) {
        this.guardLabel = guardLabel;
    }
    public String getGuardexpression() {
        return guardExpression;
    }

    public void setGuardexpression(String guardExpression) {
        this.guardExpression = guardExpression;
    }

    public research18_State getResearch18_state() {
        return research18_state;
    }

    public void setResearch18_state(research18_State research18_state) {
        this.research18_state = research18_state;
    }
    public research18_State getResearch18_state() {
        return research18_state;
    }

    public void setResearch18_state(research18_State research18_state) {
        this.research18_state = research18_state;
    }
    public research18_State getResearch18_state() {
        return research18_state;
    }

    public void setResearch18_state(research18_State research18_state) {
        this.research18_state = research18_state;
    }
    public List<research18_Action> getResearch18_actions() {
        return research18_actions;
    }

    public void addResearch18_action(Research18_action research18_action) {
        this.research18_actions.add(research18_action);
    }

}