





import java.util.List;
import java.util.ArrayList;

public class pETRI_PetriNet  {

    private String name;





    private List<pETRI_PetriNetElement> petri_petrinetelements;


    public pETRI_PetriNet(
        String name    ) {
        this.name = name;
        this.petri_petrinetelements = new ArrayList<>();
    }

    public pETRI_PetriNet(
        String name        ArrayList<pETRI_PetriNetElement> petri_petrinetelements    ) {
        this.name = name;
        this.petri_petrinetelements = petri_petrinetelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<pETRI_PetriNetElement> getPetri_petrinetelements() {
        return petri_petrinetelements;
    }

    public void addPetri_petrinetelement(Petri_petrinetelement petri_petrinetelement) {
        this.petri_petrinetelements.add(petri_petrinetelement);
    }

}