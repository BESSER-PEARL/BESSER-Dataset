





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PetriNet  {

    private String name;





    private PetriNet_Arc petrinet_arc;




    private List<PetriNet_Node> petrinet_nodes;




    private List<PetriNet_Arc> petrinet_arcs;




    private PetriNet_Node petrinet_node;


    public PetriNet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_nodes = new ArrayList<>();
        this.petrinet_arcs = new ArrayList<>();
    }

    public PetriNet_PetriNet(
        String name        ArrayList<PetriNet_Node> petrinet_nodes,        ArrayList<PetriNet_Arc> petrinet_arcs    ) {
        this.name = name;
        this.petrinet_nodes = petrinet_nodes;
        this.petrinet_arcs = petrinet_arcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(PetriNet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }
    public List<PetriNet_Node> getPetrinet_nodes() {
        return petrinet_nodes;
    }

    public void addPetrinet_node(Petrinet_node petrinet_node) {
        this.petrinet_nodes.add(petrinet_node);
    }
    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public PetriNet_Node getPetrinet_node() {
        return petrinet_node;
    }

    public void setPetrinet_node(PetriNet_Node petrinet_node) {
        this.petrinet_node = petrinet_node;
    }

}