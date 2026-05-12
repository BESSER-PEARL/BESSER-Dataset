





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_Place  {

    private String name;
    private String token;





    private PetriNetModel_ArcTP petrinetmodel_arctp;




    private List<PetriNetModel_ArcTP> petrinetmodel_arctps;


    public PetriNetModel_Place(
        String name,        String token    ) {
        this.name = name;
        this.token = token;
        this.petrinetmodel_arctps = new ArrayList<>();
    }

    public PetriNetModel_Place(
        String name,        String token        ArrayList<PetriNetModel_ArcTP> petrinetmodel_arctps    ) {
        this.name = name;
        this.token = token;
        this.petrinetmodel_arctps = petrinetmodel_arctps;
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

    public PetriNetModel_ArcTP getPetrinetmodel_arctp() {
        return petrinetmodel_arctp;
    }

    public void setPetrinetmodel_arctp(PetriNetModel_ArcTP petrinetmodel_arctp) {
        this.petrinetmodel_arctp = petrinetmodel_arctp;
    }
    public List<PetriNetModel_ArcTP> getPetrinetmodel_arctps() {
        return petrinetmodel_arctps;
    }

    public void addPetrinetmodel_arctp(Petrinetmodel_arctp petrinetmodel_arctp) {
        this.petrinetmodel_arctps.add(petrinetmodel_arctp);
    }

}