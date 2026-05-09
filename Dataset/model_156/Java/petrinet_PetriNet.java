





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {

    private String name;





    private List<petrinet_Arc> petrinet_arcs;




    private List<petrinet_Place> petrinet_places;




    private List<petrinet_Transition> petrinet_transitions;


    public petrinet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_arcs = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_PetriNet(
        String name        ArrayList<petrinet_Arc> petrinet_arcs,        ArrayList<petrinet_Place> petrinet_places,        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.name = name;
        this.petrinet_arcs = petrinet_arcs;
        this.petrinet_places = petrinet_places;
        this.petrinet_transitions = petrinet_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }

}