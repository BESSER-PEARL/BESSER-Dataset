





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Transition extends NamedElement {

    private boolean isFireable;
    private boolean isEnabled;





    private StateMachine_StateMachine statemachine_statemachine;




    private List<StateMachine_Guard> statemachine_guards;




    private StateMachine_Trigger statemachine_trigger;




    private List<StateMachine_Action> statemachine_actions;


    public StateMachine_Transition(
        boolean isFireable,        boolean isEnabled    ) {
        super(
        );
        this.isFireable = isFireable;
        this.isEnabled = isEnabled;
        this.statemachine_guards = new ArrayList<>();
        this.statemachine_actions = new ArrayList<>();
    }

    public StateMachine_Transition(
        boolean isFireable,        boolean isEnabled        ArrayList<StateMachine_Guard> statemachine_guards,        ArrayList<StateMachine_Action> statemachine_actions    ) {
        this.isFireable = isFireable;
        this.isEnabled = isEnabled;
        this.statemachine_guards = statemachine_guards;
        this.statemachine_actions = statemachine_actions;
    }

    public boolean getIsfireable() {
        return isFireable;
    }

    public void setIsfireable(boolean isFireable) {
        this.isFireable = isFireable;
    }
    public boolean getIsenabled() {
        return isEnabled;
    }

    public void setIsenabled(boolean isEnabled) {
        this.isEnabled = isEnabled;
    }

    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public List<StateMachine_Guard> getStatemachine_guards() {
        return statemachine_guards;
    }

    public void addStatemachine_guard(Statemachine_guard statemachine_guard) {
        this.statemachine_guards.add(statemachine_guard);
    }
    public StateMachine_Trigger getStatemachine_trigger() {
        return statemachine_trigger;
    }

    public void setStatemachine_trigger(StateMachine_Trigger statemachine_trigger) {
        this.statemachine_trigger = statemachine_trigger;
    }
    public List<StateMachine_Action> getStatemachine_actions() {
        return statemachine_actions;
    }

    public void addStatemachine_action(Statemachine_action statemachine_action) {
        this.statemachine_actions.add(statemachine_action);
    }

}