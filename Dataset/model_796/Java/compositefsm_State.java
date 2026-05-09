





import java.util.List;
import java.util.ArrayList;

public class compositefsm_State  {

    private String name;





    private compositefsm_FSM compositefsm_fsm;




    private compositefsm_FSM compositefsm_fsm;




    private compositefsm_FSM compositefsm_fsm;




    private compositefsm_FSM compositefsm_fsm;




    private List<compositefsm_State> compositefsm_states;




    private compositefsm_Transition compositefsm_transition;




    private List<compositefsm_Transition> compositefsm_transitions;




    private List<compositefsm_Transition> compositefsm_transitions;




    private compositefsm_Transition compositefsm_transition;




    private compositefsm_State compositefsm_state;


    public compositefsm_State(
        String name    ) {
        this.name = name;
        this.compositefsm_states = new ArrayList<>();
        this.compositefsm_transitions = new ArrayList<>();
        this.compositefsm_transitions = new ArrayList<>();
    }

    public compositefsm_State(
        String name        ArrayList<compositefsm_State> compositefsm_states,        ArrayList<compositefsm_Transition> compositefsm_transitions,        ArrayList<compositefsm_Transition> compositefsm_transitions    ) {
        this.name = name;
        this.compositefsm_states = compositefsm_states;
        this.compositefsm_transitions = compositefsm_transitions;
        this.compositefsm_transitions = compositefsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public compositefsm_FSM getCompositefsm_fsm() {
        return compositefsm_fsm;
    }

    public void setCompositefsm_fsm(compositefsm_FSM compositefsm_fsm) {
        this.compositefsm_fsm = compositefsm_fsm;
    }
    public compositefsm_FSM getCompositefsm_fsm() {
        return compositefsm_fsm;
    }

    public void setCompositefsm_fsm(compositefsm_FSM compositefsm_fsm) {
        this.compositefsm_fsm = compositefsm_fsm;
    }
    public compositefsm_FSM getCompositefsm_fsm() {
        return compositefsm_fsm;
    }

    public void setCompositefsm_fsm(compositefsm_FSM compositefsm_fsm) {
        this.compositefsm_fsm = compositefsm_fsm;
    }
    public compositefsm_FSM getCompositefsm_fsm() {
        return compositefsm_fsm;
    }

    public void setCompositefsm_fsm(compositefsm_FSM compositefsm_fsm) {
        this.compositefsm_fsm = compositefsm_fsm;
    }
    public List<compositefsm_State> getCompositefsm_states() {
        return compositefsm_states;
    }

    public void addCompositefsm_state(Compositefsm_state compositefsm_state) {
        this.compositefsm_states.add(compositefsm_state);
    }
    public compositefsm_Transition getCompositefsm_transition() {
        return compositefsm_transition;
    }

    public void setCompositefsm_transition(compositefsm_Transition compositefsm_transition) {
        this.compositefsm_transition = compositefsm_transition;
    }
    public List<compositefsm_Transition> getCompositefsm_transitions() {
        return compositefsm_transitions;
    }

    public void addCompositefsm_transition(Compositefsm_transition compositefsm_transition) {
        this.compositefsm_transitions.add(compositefsm_transition);
    }
    public List<compositefsm_Transition> getCompositefsm_transitions() {
        return compositefsm_transitions;
    }

    public void addCompositefsm_transition(Compositefsm_transition compositefsm_transition) {
        this.compositefsm_transitions.add(compositefsm_transition);
    }
    public compositefsm_Transition getCompositefsm_transition() {
        return compositefsm_transition;
    }

    public void setCompositefsm_transition(compositefsm_Transition compositefsm_transition) {
        this.compositefsm_transition = compositefsm_transition;
    }
    public compositefsm_State getCompositefsm_state() {
        return compositefsm_state;
    }

    public void setCompositefsm_state(compositefsm_State compositefsm_state) {
        this.compositefsm_state = compositefsm_state;
    }

}