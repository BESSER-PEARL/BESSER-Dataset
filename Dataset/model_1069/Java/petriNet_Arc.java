





import java.util.List;
import java.util.ArrayList;

public class petriNet_Arc extends NamedElement {

    private int weight;





    private petriNet_PetriNet petrinet_petrinet;




    private petriNet_PetriNet petrinet_petrinet;


    public petriNet_Arc(
        int weight    ) {
        super(
        );
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
    public petriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}