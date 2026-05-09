





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_PetriNet  {

    private String name;





    private List<PetriNetModel_Transition> petrinetmodel_transitions;




    private List<PetriNetModel_ArcPT> petrinetmodel_arcpts;




    private List<PetriNetModel_Place> petrinetmodel_places;




    private List<PetriNetModel_ArcTP> petrinetmodel_arctps;


    public PetriNetModel_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinetmodel_transitions = new ArrayList<>();
        this.petrinetmodel_arcpts = new ArrayList<>();
        this.petrinetmodel_places = new ArrayList<>();
        this.petrinetmodel_arctps = new ArrayList<>();
    }

    public PetriNetModel_PetriNet(
        String name        ArrayList<PetriNetModel_Transition> petrinetmodel_transitions,        ArrayList<PetriNetModel_ArcPT> petrinetmodel_arcpts,        ArrayList<PetriNetModel_Place> petrinetmodel_places,        ArrayList<PetriNetModel_ArcTP> petrinetmodel_arctps    ) {
        this.name = name;
        this.petrinetmodel_transitions = petrinetmodel_transitions;
        this.petrinetmodel_arcpts = petrinetmodel_arcpts;
        this.petrinetmodel_places = petrinetmodel_places;
        this.petrinetmodel_arctps = petrinetmodel_arctps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PetriNetModel_Transition> getPetrinetmodel_transitions() {
        return petrinetmodel_transitions;
    }

    public void addPetrinetmodel_transition(Petrinetmodel_transition petrinetmodel_transition) {
        this.petrinetmodel_transitions.add(petrinetmodel_transition);
    }
    public List<PetriNetModel_ArcPT> getPetrinetmodel_arcpts() {
        return petrinetmodel_arcpts;
    }

    public void addPetrinetmodel_arcpt(Petrinetmodel_arcpt petrinetmodel_arcpt) {
        this.petrinetmodel_arcpts.add(petrinetmodel_arcpt);
    }
    public List<PetriNetModel_Place> getPetrinetmodel_places() {
        return petrinetmodel_places;
    }

    public void addPetrinetmodel_place(Petrinetmodel_place petrinetmodel_place) {
        this.petrinetmodel_places.add(petrinetmodel_place);
    }
    public List<PetriNetModel_ArcTP> getPetrinetmodel_arctps() {
        return petrinetmodel_arctps;
    }

    public void addPetrinetmodel_arctp(Petrinetmodel_arctp petrinetmodel_arctp) {
        this.petrinetmodel_arctps.add(petrinetmodel_arctp);
    }

}