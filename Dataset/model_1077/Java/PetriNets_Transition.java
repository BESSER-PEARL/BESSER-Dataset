





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Transition extends PetriNet {






    private List<PetriNets_Place> petrinets_places;




    private List<PetriNets_Place> petrinets_places;




    private PetriNets_PetriNet petrinets_petrinet;




    private PetriNets_PetriNet petrinets_petrinet;


    public PetriNets_Transition(
    ) {
        super(
        );
        this.petrinets_places = new ArrayList<>();
        this.petrinets_places = new ArrayList<>();
    }

    public PetriNets_Transition(
        ArrayList<PetriNets_Place> petrinets_places,        ArrayList<PetriNets_Place> petrinets_places    ) {
        this.petrinets_places = petrinets_places;
        this.petrinets_places = petrinets_places;
    }


    public List<PetriNets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }
    public List<PetriNets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }
    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }
    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }

}