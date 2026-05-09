





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc  {

    private int weight;
    private String name;





    private PetriNet_Node petrinet_node;




    private PetriNet_Node petrinet_node;




    private PetriNet_PetriNet petrinet_petrinet;


    public PetriNet_Arc(
        int weight,        String name    ) {
        this.weight = weight;
        this.name = name;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_Node getPetrinet_node() {
        return petrinet_node;
    }

    public void setPetrinet_node(PetriNet_Node petrinet_node) {
        this.petrinet_node = petrinet_node;
    }
    public PetriNet_Node getPetrinet_node() {
        return petrinet_node;
    }

    public void setPetrinet_node(PetriNet_Node petrinet_node) {
        this.petrinet_node = petrinet_node;
    }
    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}