





import java.util.List;
import java.util.ArrayList;

public class TransitionToPlace  {






    private PetriNet_Transition petrinet_transition;




    private PetriNet_Place petrinet_place;


    public TransitionToPlace(
    ) {
    }



    public PetriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(PetriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public PetriNet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(PetriNet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}