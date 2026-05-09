





import java.util.List;
import java.util.ArrayList;

public class graph_DependencyGraph  {






    private List<graph_Node> graph_nodes;




    private graph_Node graph_node;




    private List<graph_Dependency> graph_dependencys;


    public graph_DependencyGraph(
    ) {
        this.graph_nodes = new ArrayList<>();
        this.graph_dependencys = new ArrayList<>();
    }

    public graph_DependencyGraph(
        ArrayList<graph_Node> graph_nodes,        ArrayList<graph_Dependency> graph_dependencys    ) {
        this.graph_nodes = graph_nodes;
        this.graph_dependencys = graph_dependencys;
    }


    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public List<graph_Dependency> getGraph_dependencys() {
        return graph_dependencys;
    }

    public void addGraph_dependency(Graph_dependency graph_dependency) {
        this.graph_dependencys.add(graph_dependency);
    }

}