





import java.util.List;
import java.util.ArrayList;

public class GraphWiki_Graph  {

    private String name;





    private List<GraphWiki_Edge> graphwiki_edges;




    private List<GraphWiki_Node> graphwiki_nodes;


    public GraphWiki_Graph(
        String name    ) {
        this.name = name;
        this.graphwiki_edges = new ArrayList<>();
        this.graphwiki_nodes = new ArrayList<>();
    }

    public GraphWiki_Graph(
        String name        ArrayList<GraphWiki_Edge> graphwiki_edges,        ArrayList<GraphWiki_Node> graphwiki_nodes    ) {
        this.name = name;
        this.graphwiki_edges = graphwiki_edges;
        this.graphwiki_nodes = graphwiki_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<GraphWiki_Edge> getGraphwiki_edges() {
        return graphwiki_edges;
    }

    public void addGraphwiki_edge(Graphwiki_edge graphwiki_edge) {
        this.graphwiki_edges.add(graphwiki_edge);
    }
    public List<GraphWiki_Node> getGraphwiki_nodes() {
        return graphwiki_nodes;
    }

    public void addGraphwiki_node(Graphwiki_node graphwiki_node) {
        this.graphwiki_nodes.add(graphwiki_node);
    }

}