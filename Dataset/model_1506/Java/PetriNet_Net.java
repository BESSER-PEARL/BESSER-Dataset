





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Net  {






    private PetriNet_Place petrinet_place;




    private List<PetriNet_Transition> petrinet_transitions;




    private PetriNet_Transition petrinet_transition;




    private List<PetriNet_Place> petrinet_places;


    public PetriNet_Net(
    ) {
        this.petrinet_transitions = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
    }

    public PetriNet_Net(
        ArrayList<PetriNet_Transition> petrinet_transitions,        ArrayList<PetriNet_Place> petrinet_places    ) {
        this.petrinet_transitions = petrinet_transitions;
        this.petrinet_places = petrinet_places;
    }


    public PetriNet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(PetriNet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public List<PetriNet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public PetriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(PetriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public List<PetriNet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}