





import java.util.List;
import java.util.ArrayList;

public class PetriNets_OutputArc  {

    private int weight;





    private PetriNets_Place petrinets_place;




    private PetriNets_PetriNet petrinets_petrinet;




    private PetriNets_Transition petrinets_transition;


    public PetriNets_OutputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public PetriNets_Place getPetrinets_place() {
        return petrinets_place;
    }

    public void setPetrinets_place(PetriNets_Place petrinets_place) {
        this.petrinets_place = petrinets_place;
    }
    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }
    public PetriNets_Transition getPetrinets_transition() {
        return petrinets_transition;
    }

    public void setPetrinets_transition(PetriNets_Transition petrinets_transition) {
        this.petrinets_transition = petrinets_transition;
    }

}