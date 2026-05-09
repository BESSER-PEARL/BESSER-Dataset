





import java.util.List;
import java.util.ArrayList;

public class graph_EnvironmentGraph  {






    private List<graph_Node> graph_nodes;




    private List<graph_Dependency> graph_dependencys;




    private List<graph_Node> graph_nodes;


    public graph_EnvironmentGraph(
    ) {
        this.graph_nodes = new ArrayList<>();
        this.graph_dependencys = new ArrayList<>();
        this.graph_nodes = new ArrayList<>();
    }

    public graph_EnvironmentGraph(
        ArrayList<graph_Node> graph_nodes,        ArrayList<graph_Dependency> graph_dependencys,        ArrayList<graph_Node> graph_nodes    ) {
        this.graph_nodes = graph_nodes;
        this.graph_dependencys = graph_dependencys;
        this.graph_nodes = graph_nodes;
    }


    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }
    public List<graph_Dependency> getGraph_dependencys() {
        return graph_dependencys;
    }

    public void addGraph_dependency(Graph_dependency graph_dependency) {
        this.graph_dependencys.add(graph_dependency);
    }
    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }

}