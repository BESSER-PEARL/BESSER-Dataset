





import java.util.List;
import java.util.ArrayList;

public class graph_DocumentRoot  {

    private String mixed;





    private List<graph_EnvironmentGraph> graph_environmentgraphs;




    private List<graph_Node> graph_nodes;




    private List<graph_Cause> graph_causes;




    private List<graph_Dependency> graph_dependencys;


    public graph_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.graph_environmentgraphs = new ArrayList<>();
        this.graph_nodes = new ArrayList<>();
        this.graph_causes = new ArrayList<>();
        this.graph_dependencys = new ArrayList<>();
    }

    public graph_DocumentRoot(
        String mixed        ArrayList<graph_EnvironmentGraph> graph_environmentgraphs,        ArrayList<graph_Node> graph_nodes,        ArrayList<graph_Cause> graph_causes,        ArrayList<graph_Dependency> graph_dependencys    ) {
        this.mixed = mixed;
        this.graph_environmentgraphs = graph_environmentgraphs;
        this.graph_nodes = graph_nodes;
        this.graph_causes = graph_causes;
        this.graph_dependencys = graph_dependencys;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<graph_EnvironmentGraph> getGraph_environmentgraphs() {
        return graph_environmentgraphs;
    }

    public void addGraph_environmentgraph(Graph_environmentgraph graph_environmentgraph) {
        this.graph_environmentgraphs.add(graph_environmentgraph);
    }
    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }
    public List<graph_Cause> getGraph_causes() {
        return graph_causes;
    }

    public void addGraph_cause(Graph_cause graph_cause) {
        this.graph_causes.add(graph_cause);
    }
    public List<graph_Dependency> getGraph_dependencys() {
        return graph_dependencys;
    }

    public void addGraph_dependency(Graph_dependency graph_dependency) {
        this.graph_dependencys.add(graph_dependency);
    }

}