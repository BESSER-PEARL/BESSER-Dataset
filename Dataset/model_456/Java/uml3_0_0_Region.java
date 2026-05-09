





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Region extends Namespace, RedefinableElement {






    private List<uml3_0_0_Transition> uml3_0_0_transitions;




    private uml3_0_0_Transition uml3_0_0_transition;




    private uml3_0_0_Region uml3_0_0_region;


    public uml3_0_0_Region(
    ) {
        super(
        );
        this.uml3_0_0_transitions = new ArrayList<>();
    }

    public uml3_0_0_Region(
        ArrayList<uml3_0_0_Transition> uml3_0_0_transitions    ) {
        this.uml3_0_0_transitions = uml3_0_0_transitions;
    }


    public List<uml3_0_0_Transition> getUml3_0_0_transitions() {
        return uml3_0_0_transitions;
    }

    public void addUml3_0_0_transition(Uml3_0_0_transition uml3_0_0_transition) {
        this.uml3_0_0_transitions.add(uml3_0_0_transition);
    }
    public uml3_0_0_Transition getUml3_0_0_transition() {
        return uml3_0_0_transition;
    }

    public void setUml3_0_0_transition(uml3_0_0_Transition uml3_0_0_transition) {
        this.uml3_0_0_transition = uml3_0_0_transition;
    }
    public uml3_0_0_Region getUml3_0_0_region() {
        return uml3_0_0_region;
    }

    public void setUml3_0_0_region(uml3_0_0_Region uml3_0_0_region) {
        this.uml3_0_0_region = uml3_0_0_region;
    }

}