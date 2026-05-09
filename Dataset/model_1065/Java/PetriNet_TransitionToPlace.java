





import java.util.List;
import java.util.ArrayList;

public class PetriNet_TransitionToPlace extends Arc {






    private Place place;




    private Transition transition;


    public PetriNet_TransitionToPlace(
    ) {
        super(
        );
    }



    public Place getPlace() {
        return place;
    }

    public void setPlace(Place place) {
        this.place = place;
    }
    public Transition getTransition() {
        return transition;
    }

    public void setTransition(Transition transition) {
        this.transition = transition;
    }

}