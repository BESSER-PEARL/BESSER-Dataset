





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_Transition  {






    private List<stateMachineDsl_Action> statemachinedsl_actions;




    private stateMachineDsl_Event statemachinedsl_event;




    private stateMachineDsl_MemberState statemachinedsl_memberstate;




    private stateMachineDsl_State statemachinedsl_state;


    public stateMachineDsl_Transition(
    ) {
        this.statemachinedsl_actions = new ArrayList<>();
    }

    public stateMachineDsl_Transition(
        ArrayList<stateMachineDsl_Action> statemachinedsl_actions    ) {
        this.statemachinedsl_actions = statemachinedsl_actions;
    }


    public List<stateMachineDsl_Action> getStatemachinedsl_actions() {
        return statemachinedsl_actions;
    }

    public void addStatemachinedsl_action(Statemachinedsl_action statemachinedsl_action) {
        this.statemachinedsl_actions.add(statemachinedsl_action);
    }
    public stateMachineDsl_Event getStatemachinedsl_event() {
        return statemachinedsl_event;
    }

    public void setStatemachinedsl_event(stateMachineDsl_Event statemachinedsl_event) {
        this.statemachinedsl_event = statemachinedsl_event;
    }
    public stateMachineDsl_MemberState getStatemachinedsl_memberstate() {
        return statemachinedsl_memberstate;
    }

    public void setStatemachinedsl_memberstate(stateMachineDsl_MemberState statemachinedsl_memberstate) {
        this.statemachinedsl_memberstate = statemachinedsl_memberstate;
    }
    public stateMachineDsl_State getStatemachinedsl_state() {
        return statemachinedsl_state;
    }

    public void setStatemachinedsl_state(stateMachineDsl_State statemachinedsl_state) {
        this.statemachinedsl_state = statemachinedsl_state;
    }

}