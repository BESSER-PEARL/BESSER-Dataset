





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition extends Element {






    private List<TransitionToPlace> transitiontoplaces;




    private List<PlaceToTransition> placetotransitions;


    public PetriNet_Transition(
    ) {
        super(
        );
        this.transitiontoplaces = new ArrayList<>();
        this.placetotransitions = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<TransitionToPlace> transitiontoplaces,        ArrayList<PlaceToTransition> placetotransitions    ) {
        this.transitiontoplaces = transitiontoplaces;
        this.placetotransitions = placetotransitions;
    }


    public List<TransitionToPlace> getTransitiontoplaces() {
        return transitiontoplaces;
    }

    public void addTransitiontoplace(Transitiontoplace transitiontoplace) {
        this.transitiontoplaces.add(transitiontoplace);
    }
    public List<PlaceToTransition> getPlacetotransitions() {
        return placetotransitions;
    }

    public void addPlacetotransition(Placetotransition placetotransition) {
        this.placetotransitions.add(placetotransition);
    }

}