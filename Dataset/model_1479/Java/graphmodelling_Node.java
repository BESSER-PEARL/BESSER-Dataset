





import java.util.List;
import java.util.ArrayList;

public class graphmodelling_Node extends Entity {






    private List<graphmodelling_Operation> graphmodelling_operations;




    private graphmodelling_Edge graphmodelling_edge;




    private List<graphmodelling_Property> graphmodelling_propertys;




    private List<graphmodelling_Node> graphmodelling_nodes;




    private graphmodelling_Graph graphmodelling_graph;




    private graphmodelling_Node graphmodelling_node;




    private graphmodelling_Edge graphmodelling_edge;


    public graphmodelling_Node(
    ) {
        super(
        );
        this.graphmodelling_operations = new ArrayList<>();
        this.graphmodelling_propertys = new ArrayList<>();
        this.graphmodelling_nodes = new ArrayList<>();
    }

    public graphmodelling_Node(
        ArrayList<graphmodelling_Operation> graphmodelling_operations,        ArrayList<graphmodelling_Property> graphmodelling_propertys,        ArrayList<graphmodelling_Node> graphmodelling_nodes    ) {
        this.graphmodelling_operations = graphmodelling_operations;
        this.graphmodelling_propertys = graphmodelling_propertys;
        this.graphmodelling_nodes = graphmodelling_nodes;
    }


    public List<graphmodelling_Operation> getGraphmodelling_operations() {
        return graphmodelling_operations;
    }

    public void addGraphmodelling_operation(Graphmodelling_operation graphmodelling_operation) {
        this.graphmodelling_operations.add(graphmodelling_operation);
    }
    public graphmodelling_Edge getGraphmodelling_edge() {
        return graphmodelling_edge;
    }

    public void setGraphmodelling_edge(graphmodelling_Edge graphmodelling_edge) {
        this.graphmodelling_edge = graphmodelling_edge;
    }
    public List<graphmodelling_Property> getGraphmodelling_propertys() {
        return graphmodelling_propertys;
    }

    public void addGraphmodelling_property(Graphmodelling_property graphmodelling_property) {
        this.graphmodelling_propertys.add(graphmodelling_property);
    }
    public List<graphmodelling_Node> getGraphmodelling_nodes() {
        return graphmodelling_nodes;
    }

    public void addGraphmodelling_node(Graphmodelling_node graphmodelling_node) {
        this.graphmodelling_nodes.add(graphmodelling_node);
    }
    public graphmodelling_Graph getGraphmodelling_graph() {
        return graphmodelling_graph;
    }

    public void setGraphmodelling_graph(graphmodelling_Graph graphmodelling_graph) {
        this.graphmodelling_graph = graphmodelling_graph;
    }
    public graphmodelling_Node getGraphmodelling_node() {
        return graphmodelling_node;
    }

    public void setGraphmodelling_node(graphmodelling_Node graphmodelling_node) {
        this.graphmodelling_node = graphmodelling_node;
    }
    public graphmodelling_Edge getGraphmodelling_edge() {
        return graphmodelling_edge;
    }

    public void setGraphmodelling_edge(graphmodelling_Edge graphmodelling_edge) {
        this.graphmodelling_edge = graphmodelling_edge;
    }

}