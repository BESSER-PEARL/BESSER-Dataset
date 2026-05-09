





import java.util.List;
import java.util.ArrayList;

public class tfsm_TimedSystem extends NamedElement {






    private List<tfsm_FSMClock> tfsm_fsmclocks;




    private List<tfsm_TFSM> tfsm_tfsms;


    public tfsm_TimedSystem(
    ) {
        super(
        );
        this.tfsm_fsmclocks = new ArrayList<>();
        this.tfsm_tfsms = new ArrayList<>();
    }

    public tfsm_TimedSystem(
        ArrayList<tfsm_FSMClock> tfsm_fsmclocks,        ArrayList<tfsm_TFSM> tfsm_tfsms    ) {
        this.tfsm_fsmclocks = tfsm_fsmclocks;
        this.tfsm_tfsms = tfsm_tfsms;
    }


    public List<tfsm_FSMClock> getTfsm_fsmclocks() {
        return tfsm_fsmclocks;
    }

    public void addTfsm_fsmclock(Tfsm_fsmclock tfsm_fsmclock) {
        this.tfsm_fsmclocks.add(tfsm_fsmclock);
    }
    public List<tfsm_TFSM> getTfsm_tfsms() {
        return tfsm_tfsms;
    }

    public void addTfsm_tfsm(Tfsm_tfsm tfsm_tfsm) {
        this.tfsm_tfsms.add(tfsm_tfsm);
    }

}