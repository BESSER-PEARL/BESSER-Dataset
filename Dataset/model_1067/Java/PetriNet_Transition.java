





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition extends Element {






    private List<TransitionToPlace> transitiontoplaces;


    public PetriNet_Transition(
    ) {
        super(
        );
        this.transitiontoplaces = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<TransitionToPlace> transitiontoplaces    ) {
        this.transitiontoplaces = transitiontoplaces;
    }


    public List<TransitionToPlace> getTransitiontoplaces() {
        return transitiontoplaces;
    }

    public void addTransitiontoplace(Transitiontoplace transitiontoplace) {
        this.transitiontoplaces.add(transitiontoplace);
    }

}