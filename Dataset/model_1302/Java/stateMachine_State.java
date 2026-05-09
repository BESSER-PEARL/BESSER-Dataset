





import java.util.List;
import java.util.ArrayList;

public class stateMachine_State extends IDElement {

    private String kind;





    private stateMachine_StateMachine statemachine_statemachine;




    private List<stateMachine_Transition> statemachine_transitions;




    private stateMachine_Transition statemachine_transition;




    private stateMachine_Transition statemachine_transition;




    private List<stateMachine_Transition> statemachine_transitions;


    public stateMachine_State(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public stateMachine_State(
        String kind        ArrayList<stateMachine_Transition> statemachine_transitions,        ArrayList<stateMachine_Transition> statemachine_transitions    ) {
        this.kind = kind;
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public List<stateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public stateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(stateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public stateMachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(stateMachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public List<stateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}