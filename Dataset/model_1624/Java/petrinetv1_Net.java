





import java.util.List;
import java.util.ArrayList;

public class petrinetv1_Net  {






    private List<petrinetv1_Place> petrinetv1_places;




    private List<petrinetv1_Transition> petrinetv1_transitions;


    public petrinetv1_Net(
    ) {
        this.petrinetv1_places = new ArrayList<>();
        this.petrinetv1_transitions = new ArrayList<>();
    }

    public petrinetv1_Net(
        ArrayList<petrinetv1_Place> petrinetv1_places,        ArrayList<petrinetv1_Transition> petrinetv1_transitions    ) {
        this.petrinetv1_places = petrinetv1_places;
        this.petrinetv1_transitions = petrinetv1_transitions;
    }


    public List<petrinetv1_Place> getPetrinetv1_places() {
        return petrinetv1_places;
    }

    public void addPetrinetv1_place(Petrinetv1_place petrinetv1_place) {
        this.petrinetv1_places.add(petrinetv1_place);
    }
    public List<petrinetv1_Transition> getPetrinetv1_transitions() {
        return petrinetv1_transitions;
    }

    public void addPetrinetv1_transition(Petrinetv1_transition petrinetv1_transition) {
        this.petrinetv1_transitions.add(petrinetv1_transition);
    }

}