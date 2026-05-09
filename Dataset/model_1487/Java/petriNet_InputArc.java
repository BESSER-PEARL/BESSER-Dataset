





import java.util.List;
import java.util.ArrayList;

public class petriNet_InputArc  {

    private int weight;





    private petriNet_PetriNet petrinet_petrinet;




    private petriNet_GenericPlace petrinet_genericplace;




    private petriNet_Transition petrinet_transition;


    public petriNet_InputArc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public petriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public petriNet_GenericPlace getPetrinet_genericplace() {
        return petrinet_genericplace;
    }

    public void setPetrinet_genericplace(petriNet_GenericPlace petrinet_genericplace) {
        this.petrinet_genericplace = petrinet_genericplace;
    }
    public petriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}