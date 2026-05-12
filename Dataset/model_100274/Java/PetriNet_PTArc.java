





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PTArc extends Arc {






    private Place place;




    private Transition transition;


    public PetriNet_PTArc(
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