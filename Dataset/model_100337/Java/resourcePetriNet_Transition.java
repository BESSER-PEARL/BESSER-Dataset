





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_Transition  {

    private String name;





    private resourcePetriNet_PetriNet resourcepetrinet_petrinet;


    public resourcePetriNet_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public resourcePetriNet_PetriNet getResourcepetrinet_petrinet() {
        return resourcepetrinet_petrinet;
    }

    public void setResourcepetrinet_petrinet(resourcePetriNet_PetriNet resourcepetrinet_petrinet) {
        this.resourcepetrinet_petrinet = resourcepetrinet_petrinet;
    }

}