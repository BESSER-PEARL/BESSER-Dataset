





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet extends NamedElement {






    private List<petrinet_Edge> petrinet_edges;




    private List<petrinet_Transition> petrinet_transitions;




    private List<petrinet_Place> petrinet_places;


    public petrinet_PetriNet(
    ) {
        super(
        );
        this.petrinet_edges = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
    }

    public petrinet_PetriNet(
        ArrayList<petrinet_Edge> petrinet_edges,        ArrayList<petrinet_Transition> petrinet_transitions,        ArrayList<petrinet_Place> petrinet_places    ) {
        this.petrinet_edges = petrinet_edges;
        this.petrinet_transitions = petrinet_transitions;
        this.petrinet_places = petrinet_places;
    }


    public List<petrinet_Edge> getPetrinet_edges() {
        return petrinet_edges;
    }

    public void addPetrinet_edge(Petrinet_edge petrinet_edge) {
        this.petrinet_edges.add(petrinet_edge);
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}