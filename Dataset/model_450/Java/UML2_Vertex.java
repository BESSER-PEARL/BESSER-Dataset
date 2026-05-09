





import java.util.List;
import java.util.ArrayList;

public class UML2_Vertex extends NamedElement {






    private List<UML2_Transition> uml2_transitions;




    private List<UML2_Transition> uml2_transitions;




    private UML2_Transition uml2_transition;




    private UML2_Region uml2_region;




    private UML2_Transition uml2_transition;




    private UML2_Region uml2_region;


    public UML2_Vertex(
    ) {
        super(
        );
        this.uml2_transitions = new ArrayList<>();
        this.uml2_transitions = new ArrayList<>();
    }

    public UML2_Vertex(
        ArrayList<UML2_Transition> uml2_transitions,        ArrayList<UML2_Transition> uml2_transitions    ) {
        this.uml2_transitions = uml2_transitions;
        this.uml2_transitions = uml2_transitions;
    }


    public List<UML2_Transition> getUml2_transitions() {
        return uml2_transitions;
    }

    public void addUml2_transition(Uml2_transition uml2_transition) {
        this.uml2_transitions.add(uml2_transition);
    }
    public List<UML2_Transition> getUml2_transitions() {
        return uml2_transitions;
    }

    public void addUml2_transition(Uml2_transition uml2_transition) {
        this.uml2_transitions.add(uml2_transition);
    }
    public UML2_Transition getUml2_transition() {
        return uml2_transition;
    }

    public void setUml2_transition(UML2_Transition uml2_transition) {
        this.uml2_transition = uml2_transition;
    }
    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }
    public UML2_Transition getUml2_transition() {
        return uml2_transition;
    }

    public void setUml2_transition(UML2_Transition uml2_transition) {
        this.uml2_transition = uml2_transition;
    }
    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }

}