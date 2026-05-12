





import java.util.List;
import java.util.ArrayList;

public class PetriNets_InputArc  {

    private int weight;





    private PetriNets_Transition petrinets_transition;


    public PetriNets_InputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public PetriNets_Transition getPetrinets_transition() {
        return petrinets_transition;
    }

    public void setPetrinets_transition(PetriNets_Transition petrinets_transition) {
        this.petrinets_transition = petrinets_transition;
    }

}