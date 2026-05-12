





import java.util.List;
import java.util.ArrayList;

public class PetriNets_PetriNet  {

    private String name;





    private List<PetriNets_Place> petrinets_places;




    private List<PetriNets_Transition> petrinets_transitions;




    private List<PetriNets_OutputArc> petrinets_outputarcs;




    private List<PetriNets_InputArc> petrinets_inputarcs;


    public PetriNets_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinets_places = new ArrayList<>();
        this.petrinets_transitions = new ArrayList<>();
        this.petrinets_outputarcs = new ArrayList<>();
        this.petrinets_inputarcs = new ArrayList<>();
    }

    public PetriNets_PetriNet(
        String name        ArrayList<PetriNets_Place> petrinets_places,        ArrayList<PetriNets_Transition> petrinets_transitions,        ArrayList<PetriNets_OutputArc> petrinets_outputarcs,        ArrayList<PetriNets_InputArc> petrinets_inputarcs    ) {
        this.name = name;
        this.petrinets_places = petrinets_places;
        this.petrinets_transitions = petrinets_transitions;
        this.petrinets_outputarcs = petrinets_outputarcs;
        this.petrinets_inputarcs = petrinets_inputarcs;
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
    public List<PetriNets_Transition> getPetrinets_transitions() {
        return petrinets_transitions;
    }

    public void addPetrinets_transition(Petrinets_transition petrinets_transition) {
        this.petrinets_transitions.add(petrinets_transition);
    }
    public List<PetriNets_OutputArc> getPetrinets_outputarcs() {
        return petrinets_outputarcs;
    }

    public void addPetrinets_outputarc(Petrinets_outputarc petrinets_outputarc) {
        this.petrinets_outputarcs.add(petrinets_outputarc);
    }
    public List<PetriNets_InputArc> getPetrinets_inputarcs() {
        return petrinets_inputarcs;
    }

    public void addPetrinets_inputarc(Petrinets_inputarc petrinets_inputarc) {
        this.petrinets_inputarcs.add(petrinets_inputarc);
    }

}