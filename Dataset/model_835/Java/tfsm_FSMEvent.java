





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMEvent extends NamedElement {






    private tfsm_TFSM tfsm_tfsm;




    private tfsm_TimedSystem tfsm_timedsystem;




    private List<tfsm_Transition> tfsm_transitions;




    private tfsm_Transition tfsm_transition;


    public tfsm_FSMEvent(
    ) {
        super(
        );
        this.tfsm_transitions = new ArrayList<>();
    }

    public tfsm_FSMEvent(
        ArrayList<tfsm_Transition> tfsm_transitions    ) {
        this.tfsm_transitions = tfsm_transitions;
    }


    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
    }
    public tfsm_TimedSystem getTfsm_timedsystem() {
        return tfsm_timedsystem;
    }

    public void setTfsm_timedsystem(tfsm_TimedSystem tfsm_timedsystem) {
        this.tfsm_timedsystem = tfsm_timedsystem;
    }
    public List<tfsm_Transition> getTfsm_transitions() {
        return tfsm_transitions;
    }

    public void addTfsm_transition(Tfsm_transition tfsm_transition) {
        this.tfsm_transitions.add(tfsm_transition);
    }
    public tfsm_Transition getTfsm_transition() {
        return tfsm_transition;
    }

    public void setTfsm_transition(tfsm_Transition tfsm_transition) {
        this.tfsm_transition = tfsm_transition;
    }

}