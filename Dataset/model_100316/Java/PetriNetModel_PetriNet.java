





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_PetriNet  {

    private String name;





    private List<PetriNetModel_ArcTP> petrinetmodel_arctps;




    private List<PetriNetModel_Place> petrinetmodel_places;


    public PetriNetModel_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinetmodel_arctps = new ArrayList<>();
        this.petrinetmodel_places = new ArrayList<>();
    }

    public PetriNetModel_PetriNet(
        String name        ArrayList<PetriNetModel_ArcTP> petrinetmodel_arctps,        ArrayList<PetriNetModel_Place> petrinetmodel_places    ) {
        this.name = name;
        this.petrinetmodel_arctps = petrinetmodel_arctps;
        this.petrinetmodel_places = petrinetmodel_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PetriNetModel_ArcTP> getPetrinetmodel_arctps() {
        return petrinetmodel_arctps;
    }

    public void addPetrinetmodel_arctp(Petrinetmodel_arctp petrinetmodel_arctp) {
        this.petrinetmodel_arctps.add(petrinetmodel_arctp);
    }
    public List<PetriNetModel_Place> getPetrinetmodel_places() {
        return petrinetmodel_places;
    }

    public void addPetrinetmodel_place(Petrinetmodel_place petrinetmodel_place) {
        this.petrinetmodel_places.add(petrinetmodel_place);
    }

}