





import java.util.List;
import java.util.ArrayList;

public class PetriNetMM0_Net  {






    private List<PetriNetMM0_Transition> petrinetmm0_transitions;




    private PetriNetMM0_Transition petrinetmm0_transition;


    public PetriNetMM0_Net(
    ) {
        this.petrinetmm0_transitions = new ArrayList<>();
    }

    public PetriNetMM0_Net(
        ArrayList<PetriNetMM0_Transition> petrinetmm0_transitions    ) {
        this.petrinetmm0_transitions = petrinetmm0_transitions;
    }


    public List<PetriNetMM0_Transition> getPetrinetmm0_transitions() {
        return petrinetmm0_transitions;
    }

    public void addPetrinetmm0_transition(Petrinetmm0_transition petrinetmm0_transition) {
        this.petrinetmm0_transitions.add(petrinetmm0_transition);
    }
    public PetriNetMM0_Transition getPetrinetmm0_transition() {
        return petrinetmm0_transition;
    }

    public void setPetrinetmm0_transition(PetriNetMM0_Transition petrinetmm0_transition) {
        this.petrinetmm0_transition = petrinetmm0_transition;
    }

}