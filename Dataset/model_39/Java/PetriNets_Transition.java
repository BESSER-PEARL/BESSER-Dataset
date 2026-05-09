





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Transition  {

    private String name;





    private PetriNets_PetriNet petrinets_petrinet;


    public PetriNets_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }

}