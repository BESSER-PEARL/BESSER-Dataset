





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PetriNet extends NamedElement {






    private PetriNet_Element petrinet_element;




    private PetriNet_Arc petrinet_arc;




    private List<PetriNet_Element> petrinet_elements;




    private List<PetriNet_Arc> petrinet_arcs;


    public PetriNet_PetriNet(
    ) {
        super(
        );
        this.petrinet_elements = new ArrayList<>();
        this.petrinet_arcs = new ArrayList<>();
    }

    public PetriNet_PetriNet(
        ArrayList<PetriNet_Element> petrinet_elements,        ArrayList<PetriNet_Arc> petrinet_arcs    ) {
        this.petrinet_elements = petrinet_elements;
        this.petrinet_arcs = petrinet_arcs;
    }


    public PetriNet_Element getPetrinet_element() {
        return petrinet_element;
    }

    public void setPetrinet_element(PetriNet_Element petrinet_element) {
        this.petrinet_element = petrinet_element;
    }
    public PetriNet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(PetriNet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }
    public List<PetriNet_Element> getPetrinet_elements() {
        return petrinet_elements;
    }

    public void addPetrinet_element(Petrinet_element petrinet_element) {
        this.petrinet_elements.add(petrinet_element);
    }
    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }

}