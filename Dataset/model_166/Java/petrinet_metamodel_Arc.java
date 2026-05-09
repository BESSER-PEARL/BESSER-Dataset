





import java.util.List;
import java.util.ArrayList;

public class petrinet_metamodel_Arc  {

    private int weight;





    private petrinet_metamodel_PetriNet petrinet_metamodel_petrinet;


    public petrinet_metamodel_Arc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public petrinet_metamodel_PetriNet getPetrinet_metamodel_petrinet() {
        return petrinet_metamodel_petrinet;
    }

    public void setPetrinet_metamodel_petrinet(petrinet_metamodel_PetriNet petrinet_metamodel_petrinet) {
        this.petrinet_metamodel_petrinet = petrinet_metamodel_petrinet;
    }

}