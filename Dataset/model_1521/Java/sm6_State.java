





import java.util.List;
import java.util.ArrayList;

public class sm6_State  {

    private String name;
    private String isFinal;





    private sm6_Transition sm6_transition;




    private sm6_Transition sm6_transition;




    private List<sm6_Transition> sm6_transitions;




    private sm6_StateMachine sm6_statemachine;




    private List<sm6_Transition> sm6_transitions;




    private sm6_StateMachine sm6_statemachine;




    private sm6_StateMachine sm6_statemachine;


    public sm6_State(
        String name,        String isFinal    ) {
        this.name = name;
        this.isFinal = isFinal;
        this.sm6_transitions = new ArrayList<>();
        this.sm6_transitions = new ArrayList<>();
    }

    public sm6_State(
        String name,        String isFinal        ArrayList<sm6_Transition> sm6_transitions,        ArrayList<sm6_Transition> sm6_transitions    ) {
        this.name = name;
        this.isFinal = isFinal;
        this.sm6_transitions = sm6_transitions;
        this.sm6_transitions = sm6_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(String isFinal) {
        this.isFinal = isFinal;
    }

    public sm6_Transition getSm6_transition() {
        return sm6_transition;
    }

    public void setSm6_transition(sm6_Transition sm6_transition) {
        this.sm6_transition = sm6_transition;
    }
    public sm6_Transition getSm6_transition() {
        return sm6_transition;
    }

    public void setSm6_transition(sm6_Transition sm6_transition) {
        this.sm6_transition = sm6_transition;
    }
    public List<sm6_Transition> getSm6_transitions() {
        return sm6_transitions;
    }

    public void addSm6_transition(Sm6_transition sm6_transition) {
        this.sm6_transitions.add(sm6_transition);
    }
    public sm6_StateMachine getSm6_statemachine() {
        return sm6_statemachine;
    }

    public void setSm6_statemachine(sm6_StateMachine sm6_statemachine) {
        this.sm6_statemachine = sm6_statemachine;
    }
    public List<sm6_Transition> getSm6_transitions() {
        return sm6_transitions;
    }

    public void addSm6_transition(Sm6_transition sm6_transition) {
        this.sm6_transitions.add(sm6_transition);
    }
    public sm6_StateMachine getSm6_statemachine() {
        return sm6_statemachine;
    }

    public void setSm6_statemachine(sm6_StateMachine sm6_statemachine) {
        this.sm6_statemachine = sm6_statemachine;
    }
    public sm6_StateMachine getSm6_statemachine() {
        return sm6_statemachine;
    }

    public void setSm6_statemachine(sm6_StateMachine sm6_statemachine) {
        this.sm6_statemachine = sm6_statemachine;
    }

}