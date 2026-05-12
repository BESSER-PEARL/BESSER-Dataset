





import java.util.List;
import java.util.ArrayList;

public class PetriNetMM2_PTArc extends Arc {






    private Place place;




    private List<Transition> transitions;


    public PetriNetMM2_PTArc(
    ) {
        super(
        );
        this.transitions = new ArrayList<>();
    }

    public PetriNetMM2_PTArc(
        ArrayList<Transition> transitions    ) {
        this.transitions = transitions;
    }


    public Place getPlace() {
        return place;
    }

    public void setPlace(Place place) {
        this.place = place;
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}