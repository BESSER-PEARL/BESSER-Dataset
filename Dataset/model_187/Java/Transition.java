





import java.util.List;
import java.util.ArrayList;

public class Transition  {






    private PetriNet_PetriNet petrinet_petrinet;




    private PetriNet_TransToPlaceArc petrinet_transtoplacearc;


    public Transition(
    ) {
    }



    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public PetriNet_TransToPlaceArc getPetrinet_transtoplacearc() {
        return petrinet_transtoplacearc;
    }

    public void setPetrinet_transtoplacearc(PetriNet_TransToPlaceArc petrinet_transtoplacearc) {
        this.petrinet_transtoplacearc = petrinet_transtoplacearc;
    }

}