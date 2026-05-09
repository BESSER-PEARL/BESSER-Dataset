





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {

    private String name;





    private List<petrinet_Arc> petrinet_arcs;




    private List<petrinet_Node> petrinet_nodes;


    public petrinet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_arcs = new ArrayList<>();
        this.petrinet_nodes = new ArrayList<>();
    }

    public petrinet_PetriNet(
        String name        ArrayList<petrinet_Arc> petrinet_arcs,        ArrayList<petrinet_Node> petrinet_nodes    ) {
        this.name = name;
        this.petrinet_arcs = petrinet_arcs;
        this.petrinet_nodes = petrinet_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public List<petrinet_Node> getPetrinet_nodes() {
        return petrinet_nodes;
    }

    public void addPetrinet_node(Petrinet_node petrinet_node) {
        this.petrinet_nodes.add(petrinet_node);
    }

}