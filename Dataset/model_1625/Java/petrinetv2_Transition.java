





import java.util.List;
import java.util.ArrayList;

public class petrinetv2_Transition  {

    private String name;





    private List<petrinetv2_Place> petrinetv2_places;




    private List<petrinetv2_Place> petrinetv2_places;




    private petrinetv2_Net petrinetv2_net;


    public petrinetv2_Transition(
        String name    ) {
        this.name = name;
        this.petrinetv2_places = new ArrayList<>();
        this.petrinetv2_places = new ArrayList<>();
    }

    public petrinetv2_Transition(
        String name        ArrayList<petrinetv2_Place> petrinetv2_places,        ArrayList<petrinetv2_Place> petrinetv2_places    ) {
        this.name = name;
        this.petrinetv2_places = petrinetv2_places;
        this.petrinetv2_places = petrinetv2_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinetv2_Place> getPetrinetv2_places() {
        return petrinetv2_places;
    }

    public void addPetrinetv2_place(Petrinetv2_place petrinetv2_place) {
        this.petrinetv2_places.add(petrinetv2_place);
    }
    public List<petrinetv2_Place> getPetrinetv2_places() {
        return petrinetv2_places;
    }

    public void addPetrinetv2_place(Petrinetv2_place petrinetv2_place) {
        this.petrinetv2_places.add(petrinetv2_place);
    }
    public petrinetv2_Net getPetrinetv2_net() {
        return petrinetv2_net;
    }

    public void setPetrinetv2_net(petrinetv2_Net petrinetv2_net) {
        this.petrinetv2_net = petrinetv2_net;
    }

}