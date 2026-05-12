





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_ArcTP  {

    private String inscription;





    private PetriNetModel_Transition petrinetmodel_transition;




    private PetriNetModel_Transition petrinetmodel_transition;




    private PetriNetModel_PetriNet petrinetmodel_petrinet;


    public PetriNetModel_ArcTP(
        String inscription    ) {
        this.inscription = inscription;
    }


    public String getInscription() {
        return inscription;
    }

    public void setInscription(String inscription) {
        this.inscription = inscription;
    }

    public PetriNetModel_Transition getPetrinetmodel_transition() {
        return petrinetmodel_transition;
    }

    public void setPetrinetmodel_transition(PetriNetModel_Transition petrinetmodel_transition) {
        this.petrinetmodel_transition = petrinetmodel_transition;
    }
    public PetriNetModel_Transition getPetrinetmodel_transition() {
        return petrinetmodel_transition;
    }

    public void setPetrinetmodel_transition(PetriNetModel_Transition petrinetmodel_transition) {
        this.petrinetmodel_transition = petrinetmodel_transition;
    }
    public PetriNetModel_PetriNet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(PetriNetModel_PetriNet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }

}