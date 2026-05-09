





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {






    private List<petrinet_Node> petrinet_nodes;




    private List<petrinet_Arc> petrinet_arcs;


    public petrinet_PetriNet(
    ) {
        this.petrinet_nodes = new ArrayList<>();
        this.petrinet_arcs = new ArrayList<>();
    }

    public petrinet_PetriNet(
        ArrayList<petrinet_Node> petrinet_nodes,        ArrayList<petrinet_Arc> petrinet_arcs    ) {
        this.petrinet_nodes = petrinet_nodes;
        this.petrinet_arcs = petrinet_arcs;
    }


    public List<petrinet_Node> getPetrinet_nodes() {
        return petrinet_nodes;
    }

    public void addPetrinet_node(Petrinet_node petrinet_node) {
        this.petrinet_nodes.add(petrinet_node);
    }
    public List<petrinet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }

}