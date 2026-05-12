





import java.util.List;
import java.util.ArrayList;

public class PetriNetMM2_TPArc extends Arc {






    private Transition transition;




    private List<Place> places;


    public PetriNetMM2_TPArc(
    ) {
        super(
        );
        this.places = new ArrayList<>();
    }

    public PetriNetMM2_TPArc(
        ArrayList<Place> places    ) {
        this.places = places;
    }


    public Transition getTransition() {
        return transition;
    }

    public void setTransition(Transition transition) {
        this.transition = transition;
    }
    public List<Place> getPlaces() {
        return places;
    }

    public void addPlace(Place place) {
        this.places.add(place);
    }

}