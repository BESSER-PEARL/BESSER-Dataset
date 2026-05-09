





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Transition  {

    private float priority;





    private List<PetriNets_Place> petrinets_places;




    private PetriNets_ArcTP petrinets_arctp;




    private PetriNets_ArcPT petrinets_arcpt;




    private List<PetriNets_Place> petrinets_places;




    private PetriNets_PetriNet petrinets_petrinet;




    private PetriNets_PetriNet petrinets_petrinet;




    private List<PetriNets_Place> petrinets_places;




    private List<PetriNets_Place> petrinets_places;




    private List<PetriNets_Place> petrinets_places;


    public PetriNets_Transition(
        float priority    ) {
        this.priority = priority;
        this.petrinets_places = new ArrayList<>();
        this.petrinets_places = new ArrayList<>();
        this.petrinets_places = new ArrayList<>();
        this.petrinets_places = new ArrayList<>();
        this.petrinets_places = new ArrayList<>();
    }

    public PetriNets_Transition(
        float priority        ArrayList<PetriNets_Place> petrinets_places,        ArrayList<PetriNets_Place> petrinets_places,        ArrayList<PetriNets_Place> petrinets_places,        ArrayList<PetriNets_Place> petrinets_places,        ArrayList<PetriNets_Place> petrinets_places    ) {
        this.priority = priority;
        this.petrinets_places = petrinets_places;
        this.petrinets_places = petrinets_places;
        this.petrinets_places = petrinets_places;
        this.petrinets_places = petrinets_places;
        this.petrinets_places = petrinets_places;
    }

    public float getPriority() {
        return priority;
    }

    public void setPriority(float priority) {
        this.priority = priority;
    }

    public List<PetriNets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }
    public PetriNets_ArcTP getPetrinets_arctp() {
        return petrinets_arctp;
    }

    public void setPetrinets_arctp(PetriNets_ArcTP petrinets_arctp) {
        this.petrinets_arctp = petrinets_arctp;
    }
    public PetriNets_ArcPT getPetrinets_arcpt() {
        return petrinets_arcpt;
    }

    public void setPetrinets_arcpt(PetriNets_ArcPT petrinets_arcpt) {
        this.petrinets_arcpt = petrinets_arcpt;
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
    public List<PetriNets_Place> getPetrinets_places() {
        return petrinets_places;
    }

    public void addPetrinets_place(Petrinets_place petrinets_place) {
        this.petrinets_places.add(petrinets_place);
    }

}