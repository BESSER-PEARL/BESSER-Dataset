





import java.util.List;
import java.util.ArrayList;

public class Graph_Edges  {

    private String name;





    private Graph_Vertices graph_vertices;




    private Graph_Graph graph_graph;




    private List<Graph_Vertices> graph_verticess;


    public Graph_Edges(
        String name    ) {
        this.name = name;
        this.graph_verticess = new ArrayList<>();
    }

    public Graph_Edges(
        String name        ArrayList<Graph_Vertices> graph_verticess    ) {
        this.name = name;
        this.graph_verticess = graph_verticess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Graph_Vertices getGraph_vertices() {
        return graph_vertices;
    }

    public void setGraph_vertices(Graph_Vertices graph_vertices) {
        this.graph_vertices = graph_vertices;
    }
    public Graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(Graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }
    public List<Graph_Vertices> getGraph_verticess() {
        return graph_verticess;
    }

    public void addGraph_vertices(Graph_vertices graph_vertices) {
        this.graph_verticess.add(graph_vertices);
    }

}