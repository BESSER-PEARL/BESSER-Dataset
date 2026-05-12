





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_GenericPlace  {

    private int numberOfTokens;
    private String name;





    private resourcePetriNet_PetriNet resourcepetrinet_petrinet;


    public resourcePetriNet_GenericPlace(
        int numberOfTokens,        String name    ) {
        this.numberOfTokens = numberOfTokens;
        this.name = name;
    }


    public int getNumberoftokens() {
        return numberOfTokens;
    }

    public void setNumberoftokens(int numberOfTokens) {
        this.numberOfTokens = numberOfTokens;
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