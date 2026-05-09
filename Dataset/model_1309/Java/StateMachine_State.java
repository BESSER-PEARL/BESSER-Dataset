





import java.util.List;
import java.util.ArrayList;

public class StateMachine_State extends NamedElement {

    private boolean isActive;
    private boolean isInitial;





    private StateMachine_Transition statemachine_transition;




    private List<StateMachine_Transition> statemachine_transitions;




    private StateMachine_StateMachine statemachine_statemachine;




    private List<StateMachine_Transition> statemachine_transitions;




    private StateMachine_StateMachine statemachine_statemachine;




    private StateMachine_Transition statemachine_transition;


    public StateMachine_State(
        boolean isActive,        boolean isInitial    ) {
        super(
        );
        this.isActive = isActive;
        this.isInitial = isInitial;
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public StateMachine_State(
        boolean isActive,        boolean isInitial        ArrayList<StateMachine_Transition> statemachine_transitions,        ArrayList<StateMachine_Transition> statemachine_transitions    ) {
        this.isActive = isActive;
        this.isInitial = isInitial;
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_transitions = statemachine_transitions;
    }

    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }

    public StateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(StateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public List<StateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public List<StateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public StateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(StateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }

}