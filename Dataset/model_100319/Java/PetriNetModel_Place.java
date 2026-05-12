





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_Place  {

    private String name;
    private String token;





    private List<PetriNetModel_ArcTP> petrinetmodel_arctps;




    private List<PetriNetModel_ArcPT> petrinetmodel_arcpts;




    private PetriNetModel_ArcPT petrinetmodel_arcpt;




    private PetriNetModel_PetriNet petrinetmodel_petrinet;




    private PetriNetModel_ArcTP petrinetmodel_arctp;


    public PetriNetModel_Place(
        String name,        String token    ) {
        this.name = name;
        this.token = token;
        this.petrinetmodel_arctps = new ArrayList<>();
        this.petrinetmodel_arcpts = new ArrayList<>();
    }

    public PetriNetModel_Place(
        String name,        String token        ArrayList<PetriNetModel_ArcTP> petrinetmodel_arctps,        ArrayList<PetriNetModel_ArcPT> petrinetmodel_arcpts    ) {
        this.name = name;
        this.token = token;
        this.petrinetmodel_arctps = petrinetmodel_arctps;
        this.petrinetmodel_arcpts = petrinetmodel_arcpts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public List<PetriNetModel_ArcTP> getPetrinetmodel_arctps() {
        return petrinetmodel_arctps;
    }

    public void addPetrinetmodel_arctp(Petrinetmodel_arctp petrinetmodel_arctp) {
        this.petrinetmodel_arctps.add(petrinetmodel_arctp);
    }
    public List<PetriNetModel_ArcPT> getPetrinetmodel_arcpts() {
        return petrinetmodel_arcpts;
    }

    public void addPetrinetmodel_arcpt(Petrinetmodel_arcpt petrinetmodel_arcpt) {
        this.petrinetmodel_arcpts.add(petrinetmodel_arcpt);
    }
    public PetriNetModel_ArcPT getPetrinetmodel_arcpt() {
        return petrinetmodel_arcpt;
    }

    public void setPetrinetmodel_arcpt(PetriNetModel_ArcPT petrinetmodel_arcpt) {
        this.petrinetmodel_arcpt = petrinetmodel_arcpt;
    }
    public PetriNetModel_PetriNet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(PetriNetModel_PetriNet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }
    public PetriNetModel_ArcTP getPetrinetmodel_arctp() {
        return petrinetmodel_arctp;
    }

    public void setPetrinetmodel_arctp(PetriNetModel_ArcTP petrinetmodel_arctp) {
        this.petrinetmodel_arctp = petrinetmodel_arctp;
    }

}