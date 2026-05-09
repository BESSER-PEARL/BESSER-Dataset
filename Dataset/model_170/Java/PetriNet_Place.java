





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place  {

    private String name;





    private PetriNet_Transition petrinet_transition;




    private PetriNet_PetriNet petrinet_petrinet;




    private PetriNet_Transition petrinet_transition;


    public PetriNet_Place(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(PetriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public PetriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(PetriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}