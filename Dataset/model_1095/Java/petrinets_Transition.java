





import java.util.List;
import java.util.ArrayList;

public class petrinets_Transition  {

    private String name;





    private petrinets_Place petrinets_place;




    private petrinets_Net petrinets_net;




    private petrinets_Net petrinets_net;




    private List<petrinets_Place> petrinets_places;




    private petrinets_Place petrinets_place;




    private List<petrinets_Place> petrinets_places;


    public petrinets_Transition(
        String name    ) {
        this.name = name;
        this.petrinets_places = new ArrayList<>();
        this.petrinets_places = new ArrayList<>();
    }

    public petrinets_Transition(
        String name        ArrayList<petrinets_Place> petrinets_places,        ArrayList<petrinets_Place> petrinets_places    ) {
        this.name = name;
        this.petrinets_places = petrinets_places;
        this.petrinets_places = petrinets_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinets_Place getPetrinets_place() {
        return petrinets_place;
    }

    public void setPetrinets_place(petrinets_Place petrinets_place) {
        this.petrinets_place = petrinets_place;
    }
    public petrinets_Net getPetrinets_net() {
        return petrinets_net;
    }

    public void setPetrinets_net(petrinets_Net petrinets_net) {
        this.petrinets_net = petrinets_net;
    }
    public petrinets_Net getPetrinets_net() {
        return petrinets_net;
    }

    public void setPetrinets_net(petrinets_Net petrinets_net) {
        this.petrinets_net = petrinets_net;
    }
    public List<petrinets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }
    public petrinets_Place getPetrinets_place() {
        return petrinets_place;
    }

    public void setPetrinets_place(petrinets_Place petrinets_place) {
        this.petrinets_place = petrinets_place;
    }
    public List<petrinets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }

}