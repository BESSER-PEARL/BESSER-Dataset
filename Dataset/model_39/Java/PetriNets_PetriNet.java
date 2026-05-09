





import java.util.List;
import java.util.ArrayList;

public class PetriNets_PetriNet  {

    private String name;





    private List<PetriNets_Place> petrinets_places;


    public PetriNets_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinets_places = new ArrayList<>();
    }

    public PetriNets_PetriNet(
        String name        ArrayList<PetriNets_Place> petrinets_places    ) {
        this.name = name;
        this.petrinets_places = petrinets_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PetriNets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }

}