





import java.util.List;
import java.util.ArrayList;

public class petri_net_Arc  {

    private String name;





    private petri_net_PetriNet petri_net_petrinet;




    private petri_net_Node petri_net_node;




    private petri_net_Node petri_net_node;


    public petri_net_Arc(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petri_net_PetriNet getPetri_net_petrinet() {
        return petri_net_petrinet;
    }

    public void setPetri_net_petrinet(petri_net_PetriNet petri_net_petrinet) {
        this.petri_net_petrinet = petri_net_petrinet;
    }
    public petri_net_Node getPetri_net_node() {
        return petri_net_node;
    }

    public void setPetri_net_node(petri_net_Node petri_net_node) {
        this.petri_net_node = petri_net_node;
    }
    public petri_net_Node getPetri_net_node() {
        return petri_net_node;
    }

    public void setPetri_net_node(petri_net_Node petri_net_node) {
        this.petri_net_node = petri_net_node;
    }

}