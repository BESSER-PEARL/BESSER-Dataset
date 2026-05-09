





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_ArcPT  {

    private String inscription;





    private List<PetriNetModel_Transition> petrinetmodel_transitions;




    private PetriNetModel_PetriNet petrinetmodel_petrinet;




    private PetriNetModel_Transition petrinetmodel_transition;


    public PetriNetModel_ArcPT(
        String inscription    ) {
        this.inscription = inscription;
        this.petrinetmodel_transitions = new ArrayList<>();
    }

    public PetriNetModel_ArcPT(
        String inscription        ArrayList<PetriNetModel_Transition> petrinetmodel_transitions    ) {
        this.inscription = inscription;
        this.petrinetmodel_transitions = petrinetmodel_transitions;
    }

    public String getInscription() {
        return inscription;
    }

    public void setInscription(String inscription) {
        this.inscription = inscription;
    }

    public List<PetriNetModel_Transition> getPetrinetmodel_transitions() {
        return petrinetmodel_transitions;
    }

    public void addPetrinetmodel_transition(Petrinetmodel_transition petrinetmodel_transition) {
        this.petrinetmodel_transitions.add(petrinetmodel_transition);
    }
    public PetriNetModel_PetriNet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(PetriNetModel_PetriNet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }
    public PetriNetModel_Transition getPetrinetmodel_transition() {
        return petrinetmodel_transition;
    }

    public void setPetrinetmodel_transition(PetriNetModel_Transition petrinetmodel_transition) {
        this.petrinetmodel_transition = petrinetmodel_transition;
    }

}