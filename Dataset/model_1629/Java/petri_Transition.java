





import java.util.List;
import java.util.ArrayList;

public class petri_Transition  {

    private String name;





    private petri_Place petri_place;




    private List<petri_Place> petri_places;


    public petri_Transition(
        String name    ) {
        this.name = name;
        this.petri_places = new ArrayList<>();
    }

    public petri_Transition(
        String name        ArrayList<petri_Place> petri_places    ) {
        this.name = name;
        this.petri_places = petri_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petri_Place getPetri_place() {
        return petri_place;
    }

    public void setPetri_place(petri_Place petri_place) {
        this.petri_place = petri_place;
    }
    public List<petri_Place> getPetri_places() {
        return petri_places;
    }

    public void addPetri_place(Petri_place petri_place) {
        this.petri_places.add(petri_place);
    }

}