





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_Transition  {

    private String name;





    private PetriNetModel_PetriNet petrinetmodel_petrinet;


    public PetriNetModel_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNetModel_PetriNet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(PetriNetModel_PetriNet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }

}