





import java.util.List;
import java.util.ArrayList;

public class petrinet_PlaceTransitionArc extends Arc {






    private petrinet_Transition petrinet_transition;




    private petrinet_PetriNet petrinet_petrinet;




    private petrinet_Place petrinet_place;


    public petrinet_PlaceTransitionArc(
    ) {
        super(
        );
    }



    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}