





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Place  {

    private int capacity;
    private int itokens;





    private PetriNets_PetriNet petrinets_petrinet;




    private List<PetriNets_Token> petrinets_tokens;




    private PetriNets_Token petrinets_token;




    private PetriNets_Transition petrinets_transition;




    private PetriNets_PetriNet petrinets_petrinet;




    private PetriNets_Transition petrinets_transition;


    public PetriNets_Place(
        int capacity,        int itokens    ) {
        this.capacity = capacity;
        this.itokens = itokens;
        this.petrinets_tokens = new ArrayList<>();
    }

    public PetriNets_Place(
        int capacity,        int itokens        ArrayList<PetriNets_Token> petrinets_tokens    ) {
        this.capacity = capacity;
        this.itokens = itokens;
        this.petrinets_tokens = petrinets_tokens;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public int getItokens() {
        return itokens;
    }

    public void setItokens(int itokens) {
        this.itokens = itokens;
    }

    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }
    public List<PetriNets_Token> getPetrinets_tokens() {
        return petrinets_tokens;
    }

    public void addPetrinets_token(Petrinets_token petrinets_token) {
        this.petrinets_tokens.add(petrinets_token);
    }
    public PetriNets_Token getPetrinets_token() {
        return petrinets_token;
    }

    public void setPetrinets_token(PetriNets_Token petrinets_token) {
        this.petrinets_token = petrinets_token;
    }
    public PetriNets_Transition getPetrinets_transition() {
        return petrinets_transition;
    }

    public void setPetrinets_transition(PetriNets_Transition petrinets_transition) {
        this.petrinets_transition = petrinets_transition;
    }
    public PetriNets_PetriNet getPetrinets_petrinet() {
        return petrinets_petrinet;
    }

    public void setPetrinets_petrinet(PetriNets_PetriNet petrinets_petrinet) {
        this.petrinets_petrinet = petrinets_petrinet;
    }
    public PetriNets_Transition getPetrinets_transition() {
        return petrinets_transition;
    }

    public void setPetrinets_transition(PetriNets_Transition petrinets_transition) {
        this.petrinets_transition = petrinets_transition;
    }

}