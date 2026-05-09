





import java.util.List;
import java.util.ArrayList;

public class tfsm_TFSM extends NamedElement {






    private List<tfsm_FSMEvent> tfsm_fsmevents;




    private tfsm_TimedSystem tfsm_timedsystem;




    private tfsm_FSMClock tfsm_fsmclock;




    private List<tfsm_Transition> tfsm_transitions;


    public tfsm_TFSM(
    ) {
        super(
        );
        this.tfsm_fsmevents = new ArrayList<>();
        this.tfsm_transitions = new ArrayList<>();
    }

    public tfsm_TFSM(
        ArrayList<tfsm_FSMEvent> tfsm_fsmevents,        ArrayList<tfsm_Transition> tfsm_transitions    ) {
        this.tfsm_fsmevents = tfsm_fsmevents;
        this.tfsm_transitions = tfsm_transitions;
    }


    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }
    public tfsm_TimedSystem getTfsm_timedsystem() {
        return tfsm_timedsystem;
    }

    public void setTfsm_timedsystem(tfsm_TimedSystem tfsm_timedsystem) {
        this.tfsm_timedsystem = tfsm_timedsystem;
    }
    public tfsm_FSMClock getTfsm_fsmclock() {
        return tfsm_fsmclock;
    }

    public void setTfsm_fsmclock(tfsm_FSMClock tfsm_fsmclock) {
        this.tfsm_fsmclock = tfsm_fsmclock;
    }
    public List<tfsm_Transition> getTfsm_transitions() {
        return tfsm_transitions;
    }

    public void addTfsm_transition(Tfsm_transition tfsm_transition) {
        this.tfsm_transitions.add(tfsm_transition);
    }

}