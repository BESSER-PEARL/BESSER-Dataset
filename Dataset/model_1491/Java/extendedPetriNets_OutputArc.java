





import java.util.List;
import java.util.ArrayList;

public class extendedPetriNets_OutputArc  {

    private int weight;





    private extendedPetriNets_PetriNet extendedpetrinets_petrinet;




    private extendedPetriNets_Transition extendedpetrinets_transition;


    public extendedPetriNets_OutputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public extendedPetriNets_PetriNet getExtendedpetrinets_petrinet() {
        return extendedpetrinets_petrinet;
    }

    public void setExtendedpetrinets_petrinet(extendedPetriNets_PetriNet extendedpetrinets_petrinet) {
        this.extendedpetrinets_petrinet = extendedpetrinets_petrinet;
    }
    public extendedPetriNets_Transition getExtendedpetrinets_transition() {
        return extendedpetrinets_transition;
    }

    public void setExtendedpetrinets_transition(extendedPetriNets_Transition extendedpetrinets_transition) {
        this.extendedpetrinets_transition = extendedpetrinets_transition;
    }

}