





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_FSMEvent extends NamedElement {

    private boolean isTriggered;





    private tfsm_plaink3_Transition tfsm_plaink3_transition;




    private List<tfsm_plaink3_Transition> tfsm_plaink3_transitions;




    private tfsm_plaink3_TimedSystem tfsm_plaink3_timedsystem;




    private tfsm_plaink3_TFSM tfsm_plaink3_tfsm;


    public tfsm_plaink3_FSMEvent(
        boolean isTriggered    ) {
        super(
        );
        this.isTriggered = isTriggered;
        this.tfsm_plaink3_transitions = new ArrayList<>();
    }

    public tfsm_plaink3_FSMEvent(
        boolean isTriggered        ArrayList<tfsm_plaink3_Transition> tfsm_plaink3_transitions    ) {
        this.isTriggered = isTriggered;
        this.tfsm_plaink3_transitions = tfsm_plaink3_transitions;
    }

    public boolean getIstriggered() {
        return isTriggered;
    }

    public void setIstriggered(boolean isTriggered) {
        this.isTriggered = isTriggered;
    }

    public tfsm_plaink3_Transition getTfsm_plaink3_transition() {
        return tfsm_plaink3_transition;
    }

    public void setTfsm_plaink3_transition(tfsm_plaink3_Transition tfsm_plaink3_transition) {
        this.tfsm_plaink3_transition = tfsm_plaink3_transition;
    }
    public List<tfsm_plaink3_Transition> getTfsm_plaink3_transitions() {
        return tfsm_plaink3_transitions;
    }

    public void addTfsm_plaink3_transition(Tfsm_plaink3_transition tfsm_plaink3_transition) {
        this.tfsm_plaink3_transitions.add(tfsm_plaink3_transition);
    }
    public tfsm_plaink3_TimedSystem getTfsm_plaink3_timedsystem() {
        return tfsm_plaink3_timedsystem;
    }

    public void setTfsm_plaink3_timedsystem(tfsm_plaink3_TimedSystem tfsm_plaink3_timedsystem) {
        this.tfsm_plaink3_timedsystem = tfsm_plaink3_timedsystem;
    }
    public tfsm_plaink3_TFSM getTfsm_plaink3_tfsm() {
        return tfsm_plaink3_tfsm;
    }

    public void setTfsm_plaink3_tfsm(tfsm_plaink3_TFSM tfsm_plaink3_tfsm) {
        this.tfsm_plaink3_tfsm = tfsm_plaink3_tfsm;
    }

}