





import java.util.List;
import java.util.ArrayList;

public class Transition  {






    private PetriNet_TransitionToPlace petrinet_transitiontoplace;




    private PetriNet_PlaceToTransition petrinet_placetotransition;


    public Transition(
    ) {
    }



    public PetriNet_TransitionToPlace getPetrinet_transitiontoplace() {
        return petrinet_transitiontoplace;
    }

    public void setPetrinet_transitiontoplace(PetriNet_TransitionToPlace petrinet_transitiontoplace) {
        this.petrinet_transitiontoplace = petrinet_transitiontoplace;
    }
    public PetriNet_PlaceToTransition getPetrinet_placetotransition() {
        return petrinet_placetotransition;
    }

    public void setPetrinet_placetotransition(PetriNet_PlaceToTransition petrinet_placetotransition) {
        this.petrinet_placetotransition = petrinet_placetotransition;
    }

}