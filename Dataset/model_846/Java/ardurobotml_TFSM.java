





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_TFSM extends RegionContainer {






    private List<ardurobotml_Transition> ardurobotml_transitions;




    private ardurobotml_FSMClock ardurobotml_fsmclock;




    private List<ardurobotml_FSMEvent> ardurobotml_fsmevents;




    private ardurobotml_TimedSystem ardurobotml_timedsystem;


    public ardurobotml_TFSM(
    ) {
        super(
        );
        this.ardurobotml_transitions = new ArrayList<>();
        this.ardurobotml_fsmevents = new ArrayList<>();
    }

    public ardurobotml_TFSM(
        ArrayList<ardurobotml_Transition> ardurobotml_transitions,        ArrayList<ardurobotml_FSMEvent> ardurobotml_fsmevents    ) {
        this.ardurobotml_transitions = ardurobotml_transitions;
        this.ardurobotml_fsmevents = ardurobotml_fsmevents;
    }


    public List<ardurobotml_Transition> getArdurobotml_transitions() {
        return ardurobotml_transitions;
    }

    public void addArdurobotml_transition(Ardurobotml_transition ardurobotml_transition) {
        this.ardurobotml_transitions.add(ardurobotml_transition);
    }
    public ardurobotml_FSMClock getArdurobotml_fsmclock() {
        return ardurobotml_fsmclock;
    }

    public void setArdurobotml_fsmclock(ardurobotml_FSMClock ardurobotml_fsmclock) {
        this.ardurobotml_fsmclock = ardurobotml_fsmclock;
    }
    public List<ardurobotml_FSMEvent> getArdurobotml_fsmevents() {
        return ardurobotml_fsmevents;
    }

    public void addArdurobotml_fsmevent(Ardurobotml_fsmevent ardurobotml_fsmevent) {
        this.ardurobotml_fsmevents.add(ardurobotml_fsmevent);
    }
    public ardurobotml_TimedSystem getArdurobotml_timedsystem() {
        return ardurobotml_timedsystem;
    }

    public void setArdurobotml_timedsystem(ardurobotml_TimedSystem ardurobotml_timedsystem) {
        this.ardurobotml_timedsystem = ardurobotml_timedsystem;
    }

}