





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_TimedSystem extends NamedElement {






    private List<tfsm_plaink3_TFSM> tfsm_plaink3_tfsms;




    private List<tfsm_plaink3_FSMClock> tfsm_plaink3_fsmclocks;


    public tfsm_plaink3_TimedSystem(
    ) {
        super(
        );
        this.tfsm_plaink3_tfsms = new ArrayList<>();
        this.tfsm_plaink3_fsmclocks = new ArrayList<>();
    }

    public tfsm_plaink3_TimedSystem(
        ArrayList<tfsm_plaink3_TFSM> tfsm_plaink3_tfsms,        ArrayList<tfsm_plaink3_FSMClock> tfsm_plaink3_fsmclocks    ) {
        this.tfsm_plaink3_tfsms = tfsm_plaink3_tfsms;
        this.tfsm_plaink3_fsmclocks = tfsm_plaink3_fsmclocks;
    }


    public List<tfsm_plaink3_TFSM> getTfsm_plaink3_tfsms() {
        return tfsm_plaink3_tfsms;
    }

    public void addTfsm_plaink3_tfsm(Tfsm_plaink3_tfsm tfsm_plaink3_tfsm) {
        this.tfsm_plaink3_tfsms.add(tfsm_plaink3_tfsm);
    }
    public List<tfsm_plaink3_FSMClock> getTfsm_plaink3_fsmclocks() {
        return tfsm_plaink3_fsmclocks;
    }

    public void addTfsm_plaink3_fsmclock(Tfsm_plaink3_fsmclock tfsm_plaink3_fsmclock) {
        this.tfsm_plaink3_fsmclocks.add(tfsm_plaink3_fsmclock);
    }

}