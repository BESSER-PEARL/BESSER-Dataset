





import java.util.List;
import java.util.ArrayList;

public class GraphML_Node extends Element {






    private List<Port> ports;




    private Graph graph;


    public GraphML_Node(
    ) {
        super(
        );
        this.ports = new ArrayList<>();
    }

    public GraphML_Node(
        ArrayList<Port> ports    ) {
        this.ports = ports;
    }


    public List<Port> getPorts() {
        return ports;
    }

    public void addPort(Port port) {
        this.ports.add(port);
    }
    public Graph getGraph() {
        return graph;
    }

    public void setGraph(Graph graph) {
        this.graph = graph;
    }

}