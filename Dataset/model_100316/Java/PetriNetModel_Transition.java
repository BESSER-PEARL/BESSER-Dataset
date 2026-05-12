





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_Transition  {

    private String name;





    private PetriNetModel_PetriNet petrinetmodel_petrinet;




    private List<PetriNetModel_ArcTP> petrinetmodel_arctps;




    private PetriNetModel_ArcTP petrinetmodel_arctp;


    public PetriNetModel_Transition(
        String name    ) {
        this.name = name;
        this.petrinetmodel_arctps = new ArrayList<>();
    }

    public PetriNetModel_Transition(
        String name        ArrayList<PetriNetModel_ArcTP> petrinetmodel_arctps    ) {
        this.name = name;
        this.petrinetmodel_arctps = petrinetmodel_arctps;
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
    public List<PetriNetModel_ArcTP> getPetrinetmodel_arctps() {
        return petrinetmodel_arctps;
    }

    public void addPetrinetmodel_arctp(Petrinetmodel_arctp petrinetmodel_arctp) {
        this.petrinetmodel_arctps.add(petrinetmodel_arctp);
    }
    public PetriNetModel_ArcTP getPetrinetmodel_arctp() {
        return petrinetmodel_arctp;
    }

    public void setPetrinetmodel_arctp(PetriNetModel_ArcTP petrinetmodel_arctp) {
        this.petrinetmodel_arctp = petrinetmodel_arctp;
    }

}