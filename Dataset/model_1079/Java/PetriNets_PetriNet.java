





import java.util.List;
import java.util.ArrayList;

public class PetriNets_PetriNet  {






    private PetriNets_Transition petrinets_transition;




    private List<PetriNets_Transition> petrinets_transitions;


    public PetriNets_PetriNet(
    ) {
        this.petrinets_transitions = new ArrayList<>();
    }

    public PetriNets_PetriNet(
        ArrayList<PetriNets_Transition> petrinets_transitions    ) {
        this.petrinets_transitions = petrinets_transitions;
    }


    public PetriNets_Transition getPetrinets_transition() {
        return petrinets_transition;
    }

    public void setPetrinets_transition(PetriNets_Transition petrinets_transition) {
        this.petrinets_transition = petrinets_transition;
    }
    public List<PetriNets_Transition> getPetrinets_transitions() {
        return petrinets_transitions;
    }

    public void addPetrinets_transition(Petrinets_transition petrinets_transition) {
        this.petrinets_transitions.add(petrinets_transition);
    }

}