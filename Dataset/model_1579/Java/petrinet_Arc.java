





import java.util.List;
import java.util.ArrayList;

public class petrinet_Arc  {

    private String name;





    private petrinet_Node petrinet_node;




    private petrinet_PetriNet petrinet_petrinet;




    private petrinet_Node petrinet_node;


    public petrinet_Arc(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_Node getPetrinet_node() {
        return petrinet_node;
    }

    public void setPetrinet_node(petrinet_Node petrinet_node) {
        this.petrinet_node = petrinet_node;
    }
    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public petrinet_Node getPetrinet_node() {
        return petrinet_node;
    }

    public void setPetrinet_node(petrinet_Node petrinet_node) {
        this.petrinet_node = petrinet_node;
    }

}