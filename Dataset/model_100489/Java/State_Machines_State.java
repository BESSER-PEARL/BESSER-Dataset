





import java.util.List;
import java.util.ArrayList;

public class State_Machines_State extends StateVertex {






    private Action action;




    private Action action;




    private Action action;




    private StateMachine statemachine;




    private List<Transition> transitions;


    public State_Machines_State(
    ) {
        super(
        );
        this.transitions = new ArrayList<>();
    }

    public State_Machines_State(
        ArrayList<Transition> transitions    ) {
        this.transitions = transitions;
    }


    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }
    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }
    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }
    public StateMachine getStatemachine() {
        return statemachine;
    }

    public void setStatemachine(StateMachine statemachine) {
        this.statemachine = statemachine;
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}