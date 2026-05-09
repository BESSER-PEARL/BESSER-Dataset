





import java.util.List;
import java.util.ArrayList;

public class petri_RedPetri  {






    private List<petri_Transition> petri_transitions;


    public petri_RedPetri(
    ) {
        this.petri_transitions = new ArrayList<>();
    }

    public petri_RedPetri(
        ArrayList<petri_Transition> petri_transitions    ) {
        this.petri_transitions = petri_transitions;
    }


    public List<petri_Transition> getPetri_transitions() {
        return petri_transitions;
    }

    public void addPetri_transition(Petri_transition petri_transition) {
        this.petri_transitions.add(petri_transition);
    }

}