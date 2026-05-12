





import java.util.List;
import java.util.ArrayList;

public class simplefsm_State  {

    private String name;
    private String action;





    private simplefsm_SimpleFiniteStateMachine simplefsm_simplefinitestatemachine;




    private simplefsm_Transition simplefsm_transition;




    private simplefsm_Transition simplefsm_transition;




    private List<simplefsm_Transition> simplefsm_transitions;




    private simplefsm_SimpleFiniteStateMachine simplefsm_simplefinitestatemachine;


    public simplefsm_State(
        String name,        String action    ) {
        this.name = name;
        this.action = action;
        this.simplefsm_transitions = new ArrayList<>();
    }

    public simplefsm_State(
        String name,        String action        ArrayList<simplefsm_Transition> simplefsm_transitions    ) {
        this.name = name;
        this.action = action;
        this.simplefsm_transitions = simplefsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public simplefsm_SimpleFiniteStateMachine getSimplefsm_simplefinitestatemachine() {
        return simplefsm_simplefinitestatemachine;
    }

    public void setSimplefsm_simplefinitestatemachine(simplefsm_SimpleFiniteStateMachine simplefsm_simplefinitestatemachine) {
        this.simplefsm_simplefinitestatemachine = simplefsm_simplefinitestatemachine;
    }
    public simplefsm_Transition getSimplefsm_transition() {
        return simplefsm_transition;
    }

    public void setSimplefsm_transition(simplefsm_Transition simplefsm_transition) {
        this.simplefsm_transition = simplefsm_transition;
    }
    public simplefsm_Transition getSimplefsm_transition() {
        return simplefsm_transition;
    }

    public void setSimplefsm_transition(simplefsm_Transition simplefsm_transition) {
        this.simplefsm_transition = simplefsm_transition;
    }
    public List<simplefsm_Transition> getSimplefsm_transitions() {
        return simplefsm_transitions;
    }

    public void addSimplefsm_transition(Simplefsm_transition simplefsm_transition) {
        this.simplefsm_transitions.add(simplefsm_transition);
    }
    public simplefsm_SimpleFiniteStateMachine getSimplefsm_simplefinitestatemachine() {
        return simplefsm_simplefinitestatemachine;
    }

    public void setSimplefsm_simplefinitestatemachine(simplefsm_SimpleFiniteStateMachine simplefsm_simplefinitestatemachine) {
        this.simplefsm_simplefinitestatemachine = simplefsm_simplefinitestatemachine;
    }

}