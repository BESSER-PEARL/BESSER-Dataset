





import java.util.List;
import java.util.ArrayList;

public class hfsm_AbstractState extends NamedElement {






    private hfsm_Transition hfsm_transition;




    private hfsm_Region hfsm_region;




    private List<hfsm_Transition> hfsm_transitions;




    private List<hfsm_Transition> hfsm_transitions;




    private hfsm_Transition hfsm_transition;




    private hfsm_Region hfsm_region;


    public hfsm_AbstractState(
    ) {
        super(
        );
        this.hfsm_transitions = new ArrayList<>();
        this.hfsm_transitions = new ArrayList<>();
    }

    public hfsm_AbstractState(
        ArrayList<hfsm_Transition> hfsm_transitions,        ArrayList<hfsm_Transition> hfsm_transitions    ) {
        this.hfsm_transitions = hfsm_transitions;
        this.hfsm_transitions = hfsm_transitions;
    }


    public hfsm_Transition getHfsm_transition() {
        return hfsm_transition;
    }

    public void setHfsm_transition(hfsm_Transition hfsm_transition) {
        this.hfsm_transition = hfsm_transition;
    }
    public hfsm_Region getHfsm_region() {
        return hfsm_region;
    }

    public void setHfsm_region(hfsm_Region hfsm_region) {
        this.hfsm_region = hfsm_region;
    }
    public List<hfsm_Transition> getHfsm_transitions() {
        return hfsm_transitions;
    }

    public void addHfsm_transition(Hfsm_transition hfsm_transition) {
        this.hfsm_transitions.add(hfsm_transition);
    }
    public List<hfsm_Transition> getHfsm_transitions() {
        return hfsm_transitions;
    }

    public void addHfsm_transition(Hfsm_transition hfsm_transition) {
        this.hfsm_transitions.add(hfsm_transition);
    }
    public hfsm_Transition getHfsm_transition() {
        return hfsm_transition;
    }

    public void setHfsm_transition(hfsm_Transition hfsm_transition) {
        this.hfsm_transition = hfsm_transition;
    }
    public hfsm_Region getHfsm_region() {
        return hfsm_region;
    }

    public void setHfsm_region(hfsm_Region hfsm_region) {
        this.hfsm_region = hfsm_region;
    }

}