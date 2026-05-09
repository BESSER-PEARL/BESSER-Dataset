





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Branch  {






    private stateMachine_Collected statemachine_collected;




    private List<stateMachine_Action> statemachine_actions;




    private stateMachine_State statemachine_state;


    public stateMachine_Branch(
    ) {
        this.statemachine_actions = new ArrayList<>();
    }

    public stateMachine_Branch(
        ArrayList<stateMachine_Action> statemachine_actions    ) {
        this.statemachine_actions = statemachine_actions;
    }


    public stateMachine_Collected getStatemachine_collected() {
        return statemachine_collected;
    }

    public void setStatemachine_collected(stateMachine_Collected statemachine_collected) {
        this.statemachine_collected = statemachine_collected;
    }
    public List<stateMachine_Action> getStatemachine_actions() {
        return statemachine_actions;
    }

    public void addStatemachine_action(Statemachine_action statemachine_action) {
        this.statemachine_actions.add(statemachine_action);
    }
    public stateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(stateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }

}