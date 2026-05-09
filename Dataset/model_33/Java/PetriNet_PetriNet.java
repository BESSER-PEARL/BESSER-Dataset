





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PetriNet extends NamedElement {






    private List<PetriNet_Arc> petrinet_arcs;




    private PetriNet_Arc petrinet_arc;


    public PetriNet_PetriNet(
    ) {
        super(
        );
        this.petrinet_arcs = new ArrayList<>();
    }

    public PetriNet_PetriNet(
        ArrayList<PetriNet_Arc> petrinet_arcs    ) {
        this.petrinet_arcs = petrinet_arcs;
    }


    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public PetriNet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(PetriNet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }

}