





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_InputArc  {

    private int weight;





    private resourcePetriNet_PetriNet resourcepetrinet_petrinet;




    private resourcePetriNet_GenericPlace resourcepetrinet_genericplace;




    private resourcePetriNet_Transition resourcepetrinet_transition;


    public resourcePetriNet_InputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public resourcePetriNet_PetriNet getResourcepetrinet_petrinet() {
        return resourcepetrinet_petrinet;
    }

    public void setResourcepetrinet_petrinet(resourcePetriNet_PetriNet resourcepetrinet_petrinet) {
        this.resourcepetrinet_petrinet = resourcepetrinet_petrinet;
    }
    public resourcePetriNet_GenericPlace getResourcepetrinet_genericplace() {
        return resourcepetrinet_genericplace;
    }

    public void setResourcepetrinet_genericplace(resourcePetriNet_GenericPlace resourcepetrinet_genericplace) {
        this.resourcepetrinet_genericplace = resourcepetrinet_genericplace;
    }
    public resourcePetriNet_Transition getResourcepetrinet_transition() {
        return resourcepetrinet_transition;
    }

    public void setResourcepetrinet_transition(resourcePetriNet_Transition resourcepetrinet_transition) {
        this.resourcepetrinet_transition = resourcepetrinet_transition;
    }

}