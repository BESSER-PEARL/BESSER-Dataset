





import java.util.List;
import java.util.ArrayList;

public class research20_Transition extends StateMachineObject {

    private String guardExpression;
    private String guardLabel;





    private List<research20_Action> research20_actions;




    private research20_State research20_state;




    private research20_State research20_state;




    private research20_State research20_state;


    public research20_Transition(
        String guardExpression,        String guardLabel    ) {
        super(
        );
        this.guardExpression = guardExpression;
        this.guardLabel = guardLabel;
        this.research20_actions = new ArrayList<>();
    }

    public research20_Transition(
        String guardExpression,        String guardLabel        ArrayList<research20_Action> research20_actions    ) {
        this.guardExpression = guardExpression;
        this.guardLabel = guardLabel;
        this.research20_actions = research20_actions;
    }

    public String getGuardexpression() {
        return guardExpression;
    }

    public void setGuardexpression(String guardExpression) {
        this.guardExpression = guardExpression;
    }
    public String getGuardlabel() {
        return guardLabel;
    }

    public void setGuardlabel(String guardLabel) {
        this.guardLabel = guardLabel;
    }

    public List<research20_Action> getResearch20_actions() {
        return research20_actions;
    }

    public void addResearch20_action(Research20_action research20_action) {
        this.research20_actions.add(research20_action);
    }
    public research20_State getResearch20_state() {
        return research20_state;
    }

    public void setResearch20_state(research20_State research20_state) {
        this.research20_state = research20_state;
    }
    public research20_State getResearch20_state() {
        return research20_state;
    }

    public void setResearch20_state(research20_State research20_state) {
        this.research20_state = research20_state;
    }
    public research20_State getResearch20_state() {
        return research20_state;
    }

    public void setResearch20_state(research20_State research20_state) {
        this.research20_state = research20_state;
    }

}