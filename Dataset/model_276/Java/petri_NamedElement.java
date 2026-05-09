





import java.util.List;
import java.util.ArrayList;

public class petri_NamedElement  {

    private String name;





    private petri_PetriNet petri_petrinet;


    public petri_NamedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petri_PetriNet getPetri_petrinet() {
        return petri_petrinet;
    }

    public void setPetri_petrinet(petri_PetriNet petri_petrinet) {
        this.petri_petrinet = petri_petrinet;
    }

}