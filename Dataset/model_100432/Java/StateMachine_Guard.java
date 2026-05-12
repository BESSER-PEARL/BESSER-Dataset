





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Guard extends NamedElement {






    private StateMachine_Transition statemachine_transition;




    private StateMachine_StateMachine statemachine_statemachine;


    public StateMachine_Guard(
    ) {
        super(
        );
    }



    public StateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(StateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}