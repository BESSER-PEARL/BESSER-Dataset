





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PlaceToTransition extends Arc {






    private Transition transition;




    private Place place;


    public PetriNet_PlaceToTransition(
    ) {
        super(
        );
    }



    public Transition getTransition() {
        return transition;
    }

    public void setTransition(Transition transition) {
        this.transition = transition;
    }
    public Place getPlace() {
        return place;
    }

    public void setPlace(Place place) {
        this.place = place;
    }

}