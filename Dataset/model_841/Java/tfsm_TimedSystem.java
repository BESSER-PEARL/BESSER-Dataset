





import java.util.List;
import java.util.ArrayList;

public class tfsm_TimedSystem extends NamedElement {






    private List<tfsm_FSMEvent> tfsm_fsmevents;




    private List<tfsm_TFSM> tfsm_tfsms;




    private List<tfsm_FSMClock> tfsm_fsmclocks;


    public tfsm_TimedSystem(
    ) {
        super(
        );
        this.tfsm_fsmevents = new ArrayList<>();
        this.tfsm_tfsms = new ArrayList<>();
        this.tfsm_fsmclocks = new ArrayList<>();
    }

    public tfsm_TimedSystem(
        ArrayList<tfsm_FSMEvent> tfsm_fsmevents,        ArrayList<tfsm_TFSM> tfsm_tfsms,        ArrayList<tfsm_FSMClock> tfsm_fsmclocks    ) {
        this.tfsm_fsmevents = tfsm_fsmevents;
        this.tfsm_tfsms = tfsm_tfsms;
        this.tfsm_fsmclocks = tfsm_fsmclocks;
    }


    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }
    public List<tfsm_TFSM> getTfsm_tfsms() {
        return tfsm_tfsms;
    }

    public void addTfsm_tfsm(Tfsm_tfsm tfsm_tfsm) {
        this.tfsm_tfsms.add(tfsm_tfsm);
    }
    public List<tfsm_FSMClock> getTfsm_fsmclocks() {
        return tfsm_fsmclocks;
    }

    public void addTfsm_fsmclock(Tfsm_fsmclock tfsm_fsmclock) {
        this.tfsm_fsmclocks.add(tfsm_fsmclock);
    }

}