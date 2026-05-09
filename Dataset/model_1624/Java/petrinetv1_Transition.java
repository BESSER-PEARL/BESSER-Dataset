





import java.util.List;
import java.util.ArrayList;

public class petrinetv1_Transition  {

    private String name;





    private List<petrinetv1_Place> petrinetv1_places;




    private List<petrinetv1_Place> petrinetv1_places;


    public petrinetv1_Transition(
        String name    ) {
        this.name = name;
        this.petrinetv1_places = new ArrayList<>();
        this.petrinetv1_places = new ArrayList<>();
    }

    public petrinetv1_Transition(
        String name        ArrayList<petrinetv1_Place> petrinetv1_places,        ArrayList<petrinetv1_Place> petrinetv1_places    ) {
        this.name = name;
        this.petrinetv1_places = petrinetv1_places;
        this.petrinetv1_places = petrinetv1_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinetv1_Place> getPetrinetv1_places() {
        return petrinetv1_places;
    }

    public void addPetrinetv1_place(Petrinetv1_place petrinetv1_place) {
        this.petrinetv1_places.add(petrinetv1_place);
    }
    public List<petrinetv1_Place> getPetrinetv1_places() {
        return petrinetv1_places;
    }

    public void addPetrinetv1_place(Petrinetv1_place petrinetv1_place) {
        this.petrinetv1_places.add(petrinetv1_place);
    }

}