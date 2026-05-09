





import java.util.List;
import java.util.ArrayList;

public class notation_HierarchicalNode extends Node {






    private List<notation_Edge> notation_edges;




    private List<notation_Node> notation_nodes;




    private notation_Edge notation_edge;




    private notation_Node notation_node;


    public notation_HierarchicalNode(
    ) {
        super(
        );
        this.notation_edges = new ArrayList<>();
        this.notation_nodes = new ArrayList<>();
    }

    public notation_HierarchicalNode(
        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Node> notation_nodes    ) {
        this.notation_edges = notation_edges;
        this.notation_nodes = notation_nodes;
    }


    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }
    public List<notation_Node> getNotation_nodes() {
        return notation_nodes;
    }

    public void addNotation_node(Notation_node notation_node) {
        this.notation_nodes.add(notation_node);
    }
    public notation_Edge getNotation_edge() {
        return notation_edge;
    }

    public void setNotation_edge(notation_Edge notation_edge) {
        this.notation_edge = notation_edge;
    }
    public notation_Node getNotation_node() {
        return notation_node;
    }

    public void setNotation_node(notation_Node notation_node) {
        this.notation_node = notation_node;
    }

}