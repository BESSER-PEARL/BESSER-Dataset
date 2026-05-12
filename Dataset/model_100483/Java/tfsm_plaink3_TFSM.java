





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_TFSM extends NamedElement {

    private int lastStateChangeStepNumber;
    private int stepNumber;





    private tfsm_plaink3_FSMClock tfsm_plaink3_fsmclock;




    private List<tfsm_plaink3_FSMEvent> tfsm_plaink3_fsmevents;




    private List<tfsm_plaink3_Transition> tfsm_plaink3_transitions;


    public tfsm_plaink3_TFSM(
        int lastStateChangeStepNumber,        int stepNumber    ) {
        super(
        );
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
        this.stepNumber = stepNumber;
        this.tfsm_plaink3_fsmevents = new ArrayList<>();
        this.tfsm_plaink3_transitions = new ArrayList<>();
    }

    public tfsm_plaink3_TFSM(
        int lastStateChangeStepNumber,        int stepNumber        ArrayList<tfsm_plaink3_FSMEvent> tfsm_plaink3_fsmevents,        ArrayList<tfsm_plaink3_Transition> tfsm_plaink3_transitions    ) {
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
        this.stepNumber = stepNumber;
        this.tfsm_plaink3_fsmevents = tfsm_plaink3_fsmevents;
        this.tfsm_plaink3_transitions = tfsm_plaink3_transitions;
    }

    public int getLaststatechangestepnumber() {
        return lastStateChangeStepNumber;
    }

    public void setLaststatechangestepnumber(int lastStateChangeStepNumber) {
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
    }
    public int getStepnumber() {
        return stepNumber;
    }

    public void setStepnumber(int stepNumber) {
        this.stepNumber = stepNumber;
    }

    public tfsm_plaink3_FSMClock getTfsm_plaink3_fsmclock() {
        return tfsm_plaink3_fsmclock;
    }

    public void setTfsm_plaink3_fsmclock(tfsm_plaink3_FSMClock tfsm_plaink3_fsmclock) {
        this.tfsm_plaink3_fsmclock = tfsm_plaink3_fsmclock;
    }
    public List<tfsm_plaink3_FSMEvent> getTfsm_plaink3_fsmevents() {
        return tfsm_plaink3_fsmevents;
    }

    public void addTfsm_plaink3_fsmevent(Tfsm_plaink3_fsmevent tfsm_plaink3_fsmevent) {
        this.tfsm_plaink3_fsmevents.add(tfsm_plaink3_fsmevent);
    }
    public List<tfsm_plaink3_Transition> getTfsm_plaink3_transitions() {
        return tfsm_plaink3_transitions;
    }

    public void addTfsm_plaink3_transition(Tfsm_plaink3_transition tfsm_plaink3_transition) {
        this.tfsm_plaink3_transitions.add(tfsm_plaink3_transition);
    }

}