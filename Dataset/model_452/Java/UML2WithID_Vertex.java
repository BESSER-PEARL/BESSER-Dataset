





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Vertex extends NamedElement {






    private UML2WithID_Transition uml2withid_transition;




    private UML2WithID_Region uml2withid_region;




    private UML2WithID_Region uml2withid_region;




    private List<UML2WithID_Transition> uml2withid_transitions;




    private UML2WithID_Transition uml2withid_transition;




    private List<UML2WithID_Transition> uml2withid_transitions;


    public UML2WithID_Vertex(
    ) {
        super(
        );
        this.uml2withid_transitions = new ArrayList<>();
        this.uml2withid_transitions = new ArrayList<>();
    }

    public UML2WithID_Vertex(
        ArrayList<UML2WithID_Transition> uml2withid_transitions,        ArrayList<UML2WithID_Transition> uml2withid_transitions    ) {
        this.uml2withid_transitions = uml2withid_transitions;
        this.uml2withid_transitions = uml2withid_transitions;
    }


    public UML2WithID_Transition getUml2withid_transition() {
        return uml2withid_transition;
    }

    public void setUml2withid_transition(UML2WithID_Transition uml2withid_transition) {
        this.uml2withid_transition = uml2withid_transition;
    }
    public UML2WithID_Region getUml2withid_region() {
        return uml2withid_region;
    }

    public void setUml2withid_region(UML2WithID_Region uml2withid_region) {
        this.uml2withid_region = uml2withid_region;
    }
    public UML2WithID_Region getUml2withid_region() {
        return uml2withid_region;
    }

    public void setUml2withid_region(UML2WithID_Region uml2withid_region) {
        this.uml2withid_region = uml2withid_region;
    }
    public List<UML2WithID_Transition> getUml2withid_transitions() {
        return uml2withid_transitions;
    }

    public void addUml2withid_transition(Uml2withid_transition uml2withid_transition) {
        this.uml2withid_transitions.add(uml2withid_transition);
    }
    public UML2WithID_Transition getUml2withid_transition() {
        return uml2withid_transition;
    }

    public void setUml2withid_transition(UML2WithID_Transition uml2withid_transition) {
        this.uml2withid_transition = uml2withid_transition;
    }
    public List<UML2WithID_Transition> getUml2withid_transitions() {
        return uml2withid_transitions;
    }

    public void addUml2withid_transition(Uml2withid_transition uml2withid_transition) {
        this.uml2withid_transitions.add(uml2withid_transition);
    }

}