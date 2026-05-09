





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition extends Element {






    private List<PlaceToTransition> placetotransitions;




    private List<TransitionToPlace> transitiontoplaces;


    public PetriNet_Transition(
    ) {
        super(
        );
        this.placetotransitions = new ArrayList<>();
        this.transitiontoplaces = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<PlaceToTransition> placetotransitions,        ArrayList<TransitionToPlace> transitiontoplaces    ) {
        this.placetotransitions = placetotransitions;
        this.transitiontoplaces = transitiontoplaces;
    }


    public List<PlaceToTransition> getPlacetotransitions() {
        return placetotransitions;
    }

    public void addPlacetotransition(Placetotransition placetotransition) {
        this.placetotransitions.add(placetotransition);
    }
    public List<TransitionToPlace> getTransitiontoplaces() {
        return transitiontoplaces;
    }

    public void addTransitiontoplace(Transitiontoplace transitiontoplace) {
        this.transitiontoplaces.add(transitiontoplace);
    }

}