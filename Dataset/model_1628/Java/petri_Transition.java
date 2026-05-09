





import java.util.List;
import java.util.ArrayList;

public class petri_Transition extends NamedElement {






    private List<petri_Place> petri_places;




    private List<petri_Place> petri_places;


    public petri_Transition(
    ) {
        super(
        );
        this.petri_places = new ArrayList<>();
        this.petri_places = new ArrayList<>();
    }

    public petri_Transition(
        ArrayList<petri_Place> petri_places,        ArrayList<petri_Place> petri_places    ) {
        this.petri_places = petri_places;
        this.petri_places = petri_places;
    }


    public List<petri_Place> getPetri_places() {
        return petri_places;
    }

    public void addPetri_place(Petri_place petri_place) {
        this.petri_places.add(petri_place);
    }
    public List<petri_Place> getPetri_places() {
        return petri_places;
    }

    public void addPetri_place(Petri_place petri_place) {
        this.petri_places.add(petri_place);
    }

}