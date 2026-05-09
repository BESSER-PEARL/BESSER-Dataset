





import java.util.List;
import java.util.ArrayList;

public class statechart_StateMachine extends IDBase {

    private String name;





    private List<statechart_Transition> statechart_transitions;




    private statechart_StateMachineRoot statechart_statemachineroot;




    private statechart_Transition statechart_transition;




    private statechart_StateMachineRoot statechart_statemachineroot;




    private statechart_StateMachineRoot statechart_statemachineroot;


    public statechart_StateMachine(
        String name    ) {
        super(
        );
        this.name = name;
        this.statechart_transitions = new ArrayList<>();
    }

    public statechart_StateMachine(
        String name        ArrayList<statechart_Transition> statechart_transitions    ) {
        this.name = name;
        this.statechart_transitions = statechart_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statechart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }
    public statechart_StateMachineRoot getStatechart_statemachineroot() {
        return statechart_statemachineroot;
    }

    public void setStatechart_statemachineroot(statechart_StateMachineRoot statechart_statemachineroot) {
        this.statechart_statemachineroot = statechart_statemachineroot;
    }
    public statechart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(statechart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public statechart_StateMachineRoot getStatechart_statemachineroot() {
        return statechart_statemachineroot;
    }

    public void setStatechart_statemachineroot(statechart_StateMachineRoot statechart_statemachineroot) {
        this.statechart_statemachineroot = statechart_statemachineroot;
    }
    public statechart_StateMachineRoot getStatechart_statemachineroot() {
        return statechart_statemachineroot;
    }

    public void setStatechart_statemachineroot(statechart_StateMachineRoot statechart_statemachineroot) {
        this.statechart_statemachineroot = statechart_statemachineroot;
    }

}