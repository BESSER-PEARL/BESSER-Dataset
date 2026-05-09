





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMEvent extends NamedElement {

    private String isTriggered;





    private tfsm_TFSM tfsm_tfsm;




    private List<tfsm_Transition> tfsm_transitions;




    private tfsm_Transition tfsm_transition;


    public tfsm_FSMEvent(
        String isTriggered    ) {
        super(
        );
        this.isTriggered = isTriggered;
        this.tfsm_transitions = new ArrayList<>();
    }

    public tfsm_FSMEvent(
        String isTriggered        ArrayList<tfsm_Transition> tfsm_transitions    ) {
        this.isTriggered = isTriggered;
        this.tfsm_transitions = tfsm_transitions;
    }

    public String getIstriggered() {
        return isTriggered;
    }

    public void setIstriggered(String isTriggered) {
        this.isTriggered = isTriggered;
    }

    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
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