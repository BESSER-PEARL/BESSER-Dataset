





import java.util.List;
import java.util.ArrayList;

public class standardPetriNets_InputArc  {

    private int weight;





    private standardPetriNets_Place standardpetrinets_place;




    private standardPetriNets_Transition standardpetrinets_transition;




    private standardPetriNets_PetriNet standardpetrinets_petrinet;


    public standardPetriNets_InputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public standardPetriNets_Place getStandardpetrinets_place() {
        return standardpetrinets_place;
    }

    public void setStandardpetrinets_place(standardPetriNets_Place standardpetrinets_place) {
        this.standardpetrinets_place = standardpetrinets_place;
    }
    public standardPetriNets_Transition getStandardpetrinets_transition() {
        return standardpetrinets_transition;
    }

    public void setStandardpetrinets_transition(standardPetriNets_Transition standardpetrinets_transition) {
        this.standardpetrinets_transition = standardpetrinets_transition;
    }
    public standardPetriNets_PetriNet getStandardpetrinets_petrinet() {
        return standardpetrinets_petrinet;
    }

    public void setStandardpetrinets_petrinet(standardPetriNets_PetriNet standardpetrinets_petrinet) {
        this.standardpetrinets_petrinet = standardpetrinets_petrinet;
    }

}