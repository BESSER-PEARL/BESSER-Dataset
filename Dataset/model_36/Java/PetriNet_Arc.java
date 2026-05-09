





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc  {

    private String name;
    private int weight;





    private PetriNet_PetriNet petrinet_petrinet;


    public PetriNet_Arc(
        String name,        int weight    ) {
        this.name = name;
        this.weight = weight;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}