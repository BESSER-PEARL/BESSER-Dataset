





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Trigger  {

    private String trigger;





    private StateMachine_State statemachine_state;




    private StateMachine_Transition statemachine_transition;


    public StateMachine_Trigger(
        String trigger    ) {
        this.trigger = trigger;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public StateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(StateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public StateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(StateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }

}