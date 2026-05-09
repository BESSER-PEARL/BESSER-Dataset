





import java.util.List;
import java.util.ArrayList;

public class graph_ElkNode extends ElkConnectableShape {

    private boolean hierarchical;





    private List<graph_ElkNode> graph_elknodes;




    private List<graph_ElkEdge> graph_elkedges;




    private graph_ElkNode graph_elknode;




    private graph_ElkEdge graph_elkedge;


    public graph_ElkNode(
        boolean hierarchical    ) {
        super(
        );
        this.hierarchical = hierarchical;
        this.graph_elknodes = new ArrayList<>();
        this.graph_elkedges = new ArrayList<>();
    }

    public graph_ElkNode(
        boolean hierarchical        ArrayList<graph_ElkNode> graph_elknodes,        ArrayList<graph_ElkEdge> graph_elkedges    ) {
        this.hierarchical = hierarchical;
        this.graph_elknodes = graph_elknodes;
        this.graph_elkedges = graph_elkedges;
    }

    public boolean getHierarchical() {
        return hierarchical;
    }

    public void setHierarchical(boolean hierarchical) {
        this.hierarchical = hierarchical;
    }

    public List<graph_ElkNode> getGraph_elknodes() {
        return graph_elknodes;
    }

    public void addGraph_elknode(Graph_elknode graph_elknode) {
        this.graph_elknodes.add(graph_elknode);
    }
    public List<graph_ElkEdge> getGraph_elkedges() {
        return graph_elkedges;
    }

    public void addGraph_elkedge(Graph_elkedge graph_elkedge) {
        this.graph_elkedges.add(graph_elkedge);
    }
    public graph_ElkNode getGraph_elknode() {
        return graph_elknode;
    }

    public void setGraph_elknode(graph_ElkNode graph_elknode) {
        this.graph_elknode = graph_elknode;
    }
    public graph_ElkEdge getGraph_elkedge() {
        return graph_elkedge;
    }

    public void setGraph_elkedge(graph_ElkEdge graph_elkedge) {
        this.graph_elkedge = graph_elkedge;
    }

}