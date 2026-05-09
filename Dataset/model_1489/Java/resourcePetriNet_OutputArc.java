





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_OutputArc  {

    private int weight;





    private resourcePetriNet_Transition resourcepetrinet_transition;


    public resourcePetriNet_OutputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public resourcePetriNet_Transition getResourcepetrinet_transition() {
        return resourcepetrinet_transition;
    }

    public void setResourcepetrinet_transition(resourcePetriNet_Transition resourcepetrinet_transition) {
        this.resourcepetrinet_transition = resourcepetrinet_transition;
    }

}