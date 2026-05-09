





import java.util.List;
import java.util.ArrayList;

public class graph_ElkEdge extends ElkGraphElement {

    private boolean connected;
    private boolean hierarchical;
    private boolean hyperedge;
    private boolean selfloop;





    private graph_ElkConnectableShape graph_elkconnectableshape;




    private List<graph_ElkConnectableShape> graph_elkconnectableshapes;




    private graph_ElkEdgeSection graph_elkedgesection;




    private List<graph_ElkEdgeSection> graph_elkedgesections;




    private List<graph_ElkConnectableShape> graph_elkconnectableshapes;




    private graph_ElkConnectableShape graph_elkconnectableshape;


    public graph_ElkEdge(
        boolean connected,        boolean hierarchical,        boolean hyperedge,        boolean selfloop    ) {
        super(
        );
        this.connected = connected;
        this.hierarchical = hierarchical;
        this.hyperedge = hyperedge;
        this.selfloop = selfloop;
        this.graph_elkconnectableshapes = new ArrayList<>();
        this.graph_elkedgesections = new ArrayList<>();
        this.graph_elkconnectableshapes = new ArrayList<>();
    }

    public graph_ElkEdge(
        boolean connected,        boolean hierarchical,        boolean hyperedge,        boolean selfloop        ArrayList<graph_ElkConnectableShape> graph_elkconnectableshapes,        ArrayList<graph_ElkEdgeSection> graph_elkedgesections,        ArrayList<graph_ElkConnectableShape> graph_elkconnectableshapes    ) {
        this.connected = connected;
        this.hierarchical = hierarchical;
        this.hyperedge = hyperedge;
        this.selfloop = selfloop;
        this.graph_elkconnectableshapes = graph_elkconnectableshapes;
        this.graph_elkedgesections = graph_elkedgesections;
        this.graph_elkconnectableshapes = graph_elkconnectableshapes;
    }

    public boolean getConnected() {
        return connected;
    }

    public void setConnected(boolean connected) {
        this.connected = connected;
    }
    public boolean getHierarchical() {
        return hierarchical;
    }

    public void setHierarchical(boolean hierarchical) {
        this.hierarchical = hierarchical;
    }
    public boolean getHyperedge() {
        return hyperedge;
    }

    public void setHyperedge(boolean hyperedge) {
        this.hyperedge = hyperedge;
    }
    public boolean getSelfloop() {
        return selfloop;
    }

    public void setSelfloop(boolean selfloop) {
        this.selfloop = selfloop;
    }

    public graph_ElkConnectableShape getGraph_elkconnectableshape() {
        return graph_elkconnectableshape;
    }

    public void setGraph_elkconnectableshape(graph_ElkConnectableShape graph_elkconnectableshape) {
        this.graph_elkconnectableshape = graph_elkconnectableshape;
    }
    public List<graph_ElkConnectableShape> getGraph_elkconnectableshapes() {
        return graph_elkconnectableshapes;
    }

    public void addGraph_elkconnectableshape(Graph_elkconnectableshape graph_elkconnectableshape) {
        this.graph_elkconnectableshapes.add(graph_elkconnectableshape);
    }
    public graph_ElkEdgeSection getGraph_elkedgesection() {
        return graph_elkedgesection;
    }

    public void setGraph_elkedgesection(graph_ElkEdgeSection graph_elkedgesection) {
        this.graph_elkedgesection = graph_elkedgesection;
    }
    public List<graph_ElkEdgeSection> getGraph_elkedgesections() {
        return graph_elkedgesections;
    }

    public void addGraph_elkedgesection(Graph_elkedgesection graph_elkedgesection) {
        this.graph_elkedgesections.add(graph_elkedgesection);
    }
    public List<graph_ElkConnectableShape> getGraph_elkconnectableshapes() {
        return graph_elkconnectableshapes;
    }

    public void addGraph_elkconnectableshape(Graph_elkconnectableshape graph_elkconnectableshape) {
        this.graph_elkconnectableshapes.add(graph_elkconnectableshape);
    }
    public graph_ElkConnectableShape getGraph_elkconnectableshape() {
        return graph_elkconnectableshape;
    }

    public void setGraph_elkconnectableshape(graph_ElkConnectableShape graph_elkconnectableshape) {
        this.graph_elkconnectableshape = graph_elkconnectableshape;
    }

}