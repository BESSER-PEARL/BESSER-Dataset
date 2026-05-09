





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {






    private List<petrinet_Place> petrinet_places;




    private List<petrinet_Transition> petrinet_transitions;




    private petrinet_Place petrinet_place;




    private petrinet_Transition petrinet_transition;


    public petrinet_PetriNet(
    ) {
        this.petrinet_places = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_PetriNet(
        ArrayList<petrinet_Place> petrinet_places,        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.petrinet_places = petrinet_places;
        this.petrinet_transitions = petrinet_transitions;
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
    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}