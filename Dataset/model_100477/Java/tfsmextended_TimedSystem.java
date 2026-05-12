





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_TimedSystem extends NamedElement {






    private List<tfsmextended_TFSM> tfsmextended_tfsms;




    private List<tfsmextended_FSMClock> tfsmextended_fsmclocks;




    private List<tfsmextended_FSMEvent> tfsmextended_fsmevents;


    public tfsmextended_TimedSystem(
    ) {
        super(
        );
        this.tfsmextended_tfsms = new ArrayList<>();
        this.tfsmextended_fsmclocks = new ArrayList<>();
        this.tfsmextended_fsmevents = new ArrayList<>();
    }

    public tfsmextended_TimedSystem(
        ArrayList<tfsmextended_TFSM> tfsmextended_tfsms,        ArrayList<tfsmextended_FSMClock> tfsmextended_fsmclocks,        ArrayList<tfsmextended_FSMEvent> tfsmextended_fsmevents    ) {
        this.tfsmextended_tfsms = tfsmextended_tfsms;
        this.tfsmextended_fsmclocks = tfsmextended_fsmclocks;
        this.tfsmextended_fsmevents = tfsmextended_fsmevents;
    }


    public List<tfsmextended_TFSM> getTfsmextended_tfsms() {
        return tfsmextended_tfsms;
    }

    public void addTfsmextended_tfsm(Tfsmextended_tfsm tfsmextended_tfsm) {
        this.tfsmextended_tfsms.add(tfsmextended_tfsm);
    }
    public List<tfsmextended_FSMClock> getTfsmextended_fsmclocks() {
        return tfsmextended_fsmclocks;
    }

    public void addTfsmextended_fsmclock(Tfsmextended_fsmclock tfsmextended_fsmclock) {
        this.tfsmextended_fsmclocks.add(tfsmextended_fsmclock);
    }
    public List<tfsmextended_FSMEvent> getTfsmextended_fsmevents() {
        return tfsmextended_fsmevents;
    }

    public void addTfsmextended_fsmevent(Tfsmextended_fsmevent tfsmextended_fsmevent) {
        this.tfsmextended_fsmevents.add(tfsmextended_fsmevent);
    }

}