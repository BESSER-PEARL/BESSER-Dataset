





import java.util.List;
import java.util.ArrayList;

public class petriNet_Place extends Element {






    private List<petriNet_PlaceToTransition> petrinet_placetotransitions;




    private petriNet_TransitionToPlace petrinet_transitiontoplace;




    private petriNet_PlaceToTransition petrinet_placetotransition;




    private List<petriNet_TransitionToPlace> petrinet_transitiontoplaces;


    public petriNet_Place(
    ) {
        super(
        );
        this.petrinet_placetotransitions = new ArrayList<>();
        this.petrinet_transitiontoplaces = new ArrayList<>();
    }

    public petriNet_Place(
        ArrayList<petriNet_PlaceToTransition> petrinet_placetotransitions,        ArrayList<petriNet_TransitionToPlace> petrinet_transitiontoplaces    ) {
        this.petrinet_placetotransitions = petrinet_placetotransitions;
        this.petrinet_transitiontoplaces = petrinet_transitiontoplaces;
    }


    public List<petriNet_PlaceToTransition> getPetrinet_placetotransitions() {
        return petrinet_placetotransitions;
    }

    public void addPetrinet_placetotransition(Petrinet_placetotransition petrinet_placetotransition) {
        this.petrinet_placetotransitions.add(petrinet_placetotransition);
    }
    public petriNet_TransitionToPlace getPetrinet_transitiontoplace() {
        return petrinet_transitiontoplace;
    }

    public void setPetrinet_transitiontoplace(petriNet_TransitionToPlace petrinet_transitiontoplace) {
        this.petrinet_transitiontoplace = petrinet_transitiontoplace;
    }
    public petriNet_PlaceToTransition getPetrinet_placetotransition() {
        return petrinet_placetotransition;
    }

    public void setPetrinet_placetotransition(petriNet_PlaceToTransition petrinet_placetotransition) {
        this.petrinet_placetotransition = petrinet_placetotransition;
    }
    public List<petriNet_TransitionToPlace> getPetrinet_transitiontoplaces() {
        return petrinet_transitiontoplaces;
    }

    public void addPetrinet_transitiontoplace(Petrinet_transitiontoplace petrinet_transitiontoplace) {
        this.petrinet_transitiontoplaces.add(petrinet_transitiontoplace);
    }

}