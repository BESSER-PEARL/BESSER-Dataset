





import java.util.List;
import java.util.ArrayList;

public class tfsm_TFSM extends NamedElement {






    private List<tfsm_State> tfsm_states;




    private List<tfsm_FSMEvent> tfsm_fsmevents;




    private tfsm_State tfsm_state;




    private tfsm_State tfsm_state;




    private tfsm_FSMClock tfsm_fsmclock;




    private tfsm_State tfsm_state;




    private List<tfsm_Transition> tfsm_transitions;


    public tfsm_TFSM(
    ) {
        super(
        );
        this.tfsm_states = new ArrayList<>();
        this.tfsm_fsmevents = new ArrayList<>();
        this.tfsm_transitions = new ArrayList<>();
    }

    public tfsm_TFSM(
        ArrayList<tfsm_State> tfsm_states,        ArrayList<tfsm_FSMEvent> tfsm_fsmevents,        ArrayList<tfsm_Transition> tfsm_transitions    ) {
        this.tfsm_states = tfsm_states;
        this.tfsm_fsmevents = tfsm_fsmevents;
        this.tfsm_transitions = tfsm_transitions;
    }


    public List<tfsm_State> getTfsm_states() {
        return tfsm_states;
    }

    public void addTfsm_state(Tfsm_state tfsm_state) {
        this.tfsm_states.add(tfsm_state);
    }
    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_FSMClock getTfsm_fsmclock() {
        return tfsm_fsmclock;
    }

    public void setTfsm_fsmclock(tfsm_FSMClock tfsm_fsmclock) {
        this.tfsm_fsmclock = tfsm_fsmclock;
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public List<tfsm_Transition> getTfsm_transitions() {
        return tfsm_transitions;
    }

    public void addTfsm_transition(Tfsm_transition tfsm_transition) {
        this.tfsm_transitions.add(tfsm_transition);
    }

}