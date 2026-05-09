





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_PObject  {

    private int id;





    private PetriNetModel_PetriNet petrinetmodel_petrinet;


    public PetriNetModel_PObject(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public PetriNetModel_PetriNet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(PetriNetModel_PetriNet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }

}