





import java.util.List;
import java.util.ArrayList;

public class graph_Vertex  {

    private String internalId;





    private graph_Graph graph_graph;




    private List<graph_Vertex> graph_vertexs;




    private graph_Graph graph_graph;


    public graph_Vertex(
        String internalId    ) {
        this.internalId = internalId;
        this.graph_vertexs = new ArrayList<>();
    }

    public graph_Vertex(
        String internalId        ArrayList<graph_Vertex> graph_vertexs    ) {
        this.internalId = internalId;
        this.graph_vertexs = graph_vertexs;
    }

    public String getInternalid() {
        return internalId;
    }

    public void setInternalid(String internalId) {
        this.internalId = internalId;
    }

    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }
    public List<graph_Vertex> getGraph_vertexs() {
        return graph_vertexs;
    }

    public void addGraph_vertex(Graph_vertex graph_vertex) {
        this.graph_vertexs.add(graph_vertex);
    }
    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }

}