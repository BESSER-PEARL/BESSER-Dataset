





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMEvent extends NamedElement {






    private tfsm_TFSM tfsm_tfsm;




    private tfsm_Transition tfsm_transition;




    private List<tfsm_Transition> tfsm_transitions;


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
    public tfsm_Transition getTfsm_transition() {
        return tfsm_transition;
    }

    public void setTfsm_transition(tfsm_Transition tfsm_transition) {
        this.tfsm_transition = tfsm_transition;
    }
    public List<tfsm_Transition> getTfsm_transitions() {
        return tfsm_transitions;
    }

    public void addTfsm_transition(Tfsm_transition tfsm_transition) {
        this.tfsm_transitions.add(tfsm_transition);
    }

}