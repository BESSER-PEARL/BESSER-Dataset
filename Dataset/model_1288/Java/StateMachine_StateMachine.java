





import java.util.List;
import java.util.ArrayList;

public class StateMachine_StateMachine  {






    private List<StateMachine_Transition> statemachine_transitions;




    private List<StateMachine_StateVertex> statemachine_statevertexs;


    public StateMachine_StateMachine(
    ) {
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_statevertexs = new ArrayList<>();
    }

    public StateMachine_StateMachine(
        ArrayList<StateMachine_Transition> statemachine_transitions,        ArrayList<StateMachine_StateVertex> statemachine_statevertexs    ) {
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_statevertexs = statemachine_statevertexs;
    }


    public List<StateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public List<StateMachine_StateVertex> getStatemachine_statevertexs() {
        return statemachine_statevertexs;
    }

    public void addStatemachine_statevertex(Statemachine_statevertex statemachine_statevertex) {
        this.statemachine_statevertexs.add(statemachine_statevertex);
    }

}