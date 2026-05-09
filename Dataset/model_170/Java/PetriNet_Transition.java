





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition  {

    private String name;





    private PetriNet_PetriNet petrinet_petrinet;


    public PetriNet_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}