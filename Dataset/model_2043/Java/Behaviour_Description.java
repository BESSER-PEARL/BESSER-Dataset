





import java.util.List;
import java.util.ArrayList;

public class Behaviour_Description extends Identifier {






    private List<Behaviour_Place> behaviour_places;




    private List<Behaviour_Transition> behaviour_transitions;


    public Behaviour_Description(
    ) {
        super(
        );
        this.behaviour_places = new ArrayList<>();
        this.behaviour_transitions = new ArrayList<>();
    }

    public Behaviour_Description(
        ArrayList<Behaviour_Place> behaviour_places,        ArrayList<Behaviour_Transition> behaviour_transitions    ) {
        this.behaviour_places = behaviour_places;
        this.behaviour_transitions = behaviour_transitions;
    }


    public List<Behaviour_Place> getBehaviour_places() {
        return behaviour_places;
    }

    public void addBehaviour_place(Behaviour_place behaviour_place) {
        this.behaviour_places.add(behaviour_place);
    }
    public List<Behaviour_Transition> getBehaviour_transitions() {
        return behaviour_transitions;
    }

    public void addBehaviour_transition(Behaviour_transition behaviour_transition) {
        this.behaviour_transitions.add(behaviour_transition);
    }

}