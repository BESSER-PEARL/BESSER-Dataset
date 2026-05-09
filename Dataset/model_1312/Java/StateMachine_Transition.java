





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Transition  {

    private String action;
    private String name;
    private String trigger;
    private int id;





    private StateMachine_State statemachine_state;




    private StateMachine_WashingMachine statemachine_washingmachine;




    private StateMachine_State statemachine_state;




    private StateMachine_State statemachine_state;


    public StateMachine_Transition(
        String action,        String name,        String trigger,        int id    ) {
        this.action = action;
        this.name = name;
        this.trigger = trigger;
        this.id = id;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public StateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(StateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public StateMachine_WashingMachine getStatemachine_washingmachine() {
        return statemachine_washingmachine;
    }

    public void setStatemachine_washingmachine(StateMachine_WashingMachine statemachine_washingmachine) {
        this.statemachine_washingmachine = statemachine_washingmachine;
    }
    public StateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(StateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public StateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(StateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }

}