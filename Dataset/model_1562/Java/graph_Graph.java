





import java.util.List;
import java.util.ArrayList;

public class graph_Graph extends Identifiable {

    private int numNodes;
    private int numGraphLabels;
    private int numEdges;
    private int numNodeLabels;
    private int numDynamicLabels;





    private List<graph_Decorator> graph_decorators;


    public graph_Graph(
        int numNodes,        int numGraphLabels,        int numEdges,        int numNodeLabels,        int numDynamicLabels    ) {
        super(
        );
        this.numNodes = numNodes;
        this.numGraphLabels = numGraphLabels;
        this.numEdges = numEdges;
        this.numNodeLabels = numNodeLabels;
        this.numDynamicLabels = numDynamicLabels;
        this.graph_decorators = new ArrayList<>();
    }

    public graph_Graph(
        int numNodes,        int numGraphLabels,        int numEdges,        int numNodeLabels,        int numDynamicLabels        ArrayList<graph_Decorator> graph_decorators    ) {
        this.numNodes = numNodes;
        this.numGraphLabels = numGraphLabels;
        this.numEdges = numEdges;
        this.numNodeLabels = numNodeLabels;
        this.numDynamicLabels = numDynamicLabels;
        this.graph_decorators = graph_decorators;
    }

    public int getNumnodes() {
        return numNodes;
    }

    public void setNumnodes(int numNodes) {
        this.numNodes = numNodes;
    }
    public int getNumgraphlabels() {
        return numGraphLabels;
    }

    public void setNumgraphlabels(int numGraphLabels) {
        this.numGraphLabels = numGraphLabels;
    }
    public int getNumedges() {
        return numEdges;
    }

    public void setNumedges(int numEdges) {
        this.numEdges = numEdges;
    }
    public int getNumnodelabels() {
        return numNodeLabels;
    }

    public void setNumnodelabels(int numNodeLabels) {
        this.numNodeLabels = numNodeLabels;
    }
    public int getNumdynamiclabels() {
        return numDynamicLabels;
    }

    public void setNumdynamiclabels(int numDynamicLabels) {
        this.numDynamicLabels = numDynamicLabels;
    }

    public List<graph_Decorator> getGraph_decorators() {
        return graph_decorators;
    }

    public void addGraph_decorator(Graph_decorator graph_decorator) {
        this.graph_decorators.add(graph_decorator);
    }

}