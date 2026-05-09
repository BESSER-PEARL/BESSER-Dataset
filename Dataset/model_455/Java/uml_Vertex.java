





import java.util.List;
import java.util.ArrayList;

public class uml_Vertex extends NamedElement {






    private uml_Region uml_region;




    private uml_Transition uml_transition;




    private List<uml_Transition> uml_transitions;




    private uml_Transition uml_transition;




    private uml_Region uml_region;




    private List<uml_Transition> uml_transitions;


    public uml_Vertex(
    ) {
        super(
        );
        this.uml_transitions = new ArrayList<>();
        this.uml_transitions = new ArrayList<>();
    }

    public uml_Vertex(
        ArrayList<uml_Transition> uml_transitions,        ArrayList<uml_Transition> uml_transitions    ) {
        this.uml_transitions = uml_transitions;
        this.uml_transitions = uml_transitions;
    }


    public uml_Region getUml_region() {
        return uml_region;
    }

    public void setUml_region(uml_Region uml_region) {
        this.uml_region = uml_region;
    }
    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }
    public List<uml_Transition> getUml_transitions() {
        return uml_transitions;
    }

    public void addUml_transition(Uml_transition uml_transition) {
        this.uml_transitions.add(uml_transition);
    }
    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }
    public uml_Region getUml_region() {
        return uml_region;
    }

    public void setUml_region(uml_Region uml_region) {
        this.uml_region = uml_region;
    }
    public List<uml_Transition> getUml_transitions() {
        return uml_transitions;
    }

    public void addUml_transition(Uml_transition uml_transition) {
        this.uml_transitions.add(uml_transition);
    }

}