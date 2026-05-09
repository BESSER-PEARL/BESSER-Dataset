





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Arc  {

    private int weight;





    private PetriNets_PetriNet petrinets_petrinet;


    public PetriNets_Arc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }

}