





import java.util.List;
import java.util.ArrayList;

public class tfsm_TimedSystem extends NamedElement {






    private List<tfsm_FSMClock> tfsm_fsmclocks;




    private List<tfsm_FSMEvent> tfsm_fsmevents;


    public tfsm_TimedSystem(
    ) {
        super(
        );
        this.tfsm_fsmclocks = new ArrayList<>();
        this.tfsm_fsmevents = new ArrayList<>();
    }

    public tfsm_TimedSystem(
        ArrayList<tfsm_FSMClock> tfsm_fsmclocks,        ArrayList<tfsm_FSMEvent> tfsm_fsmevents    ) {
        this.tfsm_fsmclocks = tfsm_fsmclocks;
        this.tfsm_fsmevents = tfsm_fsmevents;
    }


    public List<tfsm_FSMClock> getTfsm_fsmclocks() {
        return tfsm_fsmclocks;
    }

    public void addTfsm_fsmclock(Tfsm_fsmclock tfsm_fsmclock) {
        this.tfsm_fsmclocks.add(tfsm_fsmclock);
    }
    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }

}