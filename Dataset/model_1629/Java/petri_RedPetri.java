





import java.util.List;
import java.util.ArrayList;

public class petri_RedPetri  {






    private List<petri_Transition> petri_transitions;




    private List<petri_Place> petri_places;


    public petri_RedPetri(
    ) {
        this.petri_transitions = new ArrayList<>();
        this.petri_places = new ArrayList<>();
    }

    public petri_RedPetri(
        ArrayList<petri_Transition> petri_transitions,        ArrayList<petri_Place> petri_places    ) {
        this.petri_transitions = petri_transitions;
        this.petri_places = petri_places;
    }


    public List<petri_Transition> getPetri_transitions() {
        return petri_transitions;
    }

    public void addPetri_transition(Petri_transition petri_transition) {
        this.petri_transitions.add(petri_transition);
    }
    public List<petri_Place> getPetri_places() {
        return petri_places;
    }

    public void addPetri_place(Petri_place petri_place) {
        this.petri_places.add(petri_place);
    }

}