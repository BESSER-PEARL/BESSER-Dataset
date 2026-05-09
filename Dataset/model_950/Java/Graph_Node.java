





import java.util.List;
import java.util.ArrayList;

public class Graph_Node  {

    private String name;





    private Graph_Edge graph_edge;




    private Graph_Graph graph_graph;




    private Graph_Edge graph_edge;




    private List<Graph_Edge> graph_edges;




    private List<Graph_Edge> graph_edges;


    public Graph_Node(
        String name    ) {
        this.name = name;
        this.graph_edges = new ArrayList<>();
        this.graph_edges = new ArrayList<>();
    }

    public Graph_Node(
        String name        ArrayList<Graph_Edge> graph_edges,        ArrayList<Graph_Edge> graph_edges    ) {
        this.name = name;
        this.graph_edges = graph_edges;
        this.graph_edges = graph_edges;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(Graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }
    public Graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(Graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }
    public Graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(Graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }
    public List<Graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }
    public List<Graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }

}