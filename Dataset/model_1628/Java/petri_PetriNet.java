





import java.util.List;
import java.util.ArrayList;

public class petri_PetriNet  {






    private List<petri_NamedElement> petri_namedelements;


    public petri_PetriNet(
    ) {
        this.petri_namedelements = new ArrayList<>();
    }

    public petri_PetriNet(
        ArrayList<petri_NamedElement> petri_namedelements    ) {
        this.petri_namedelements = petri_namedelements;
    }


    public List<petri_NamedElement> getPetri_namedelements() {
        return petri_namedelements;
    }

    public void addPetri_namedelement(Petri_namedelement petri_namedelement) {
        this.petri_namedelements.add(petri_namedelement);
    }

}