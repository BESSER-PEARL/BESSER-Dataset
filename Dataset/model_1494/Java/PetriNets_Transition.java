





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Transition extends Node {






    private List<PetriNets_Place> petrinets_places;




    private PetriNets_TPArc petrinets_tparc;




    private List<PetriNets_Place> petrinets_places;




    private PetriNets_PTArc petrinets_ptarc;


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
    public PetriNets_TPArc getPetrinets_tparc() {
        return petrinets_tparc;
    }

    public void setPetrinets_tparc(PetriNets_TPArc petrinets_tparc) {
        this.petrinets_tparc = petrinets_tparc;
    }
    public List<PetriNets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }
    public PetriNets_PTArc getPetrinets_ptarc() {
        return petrinets_ptarc;
    }

    public void setPetrinets_ptarc(PetriNets_PTArc petrinets_ptarc) {
        this.petrinets_ptarc = petrinets_ptarc;
    }

}