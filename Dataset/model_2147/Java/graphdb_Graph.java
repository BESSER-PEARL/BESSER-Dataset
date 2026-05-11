





import java.util.List;
import java.util.ArrayList;

public class graphdb_Graph  {

    private String rawDatabase;





    private graphdb_Vertex graphdb_vertex;




    private List<graphdb_Vertex> graphdb_vertexs;




    private graphdb_Edge graphdb_edge;




    private List<graphdb_Edge> graphdb_edges;


    public graphdb_Graph(
        String rawDatabase    ) {
        this.rawDatabase = rawDatabase;
        this.graphdb_vertexs = new ArrayList<>();
        this.graphdb_edges = new ArrayList<>();
    }

    public graphdb_Graph(
        String rawDatabase        ArrayList<graphdb_Vertex> graphdb_vertexs,        ArrayList<graphdb_Edge> graphdb_edges    ) {
        this.rawDatabase = rawDatabase;
        this.graphdb_vertexs = graphdb_vertexs;
        this.graphdb_edges = graphdb_edges;
    }

    public String getRawdatabase() {
        return rawDatabase;
    }

    public void setRawdatabase(String rawDatabase) {
        this.rawDatabase = rawDatabase;
    }

    public graphdb_Vertex getGraphdb_vertex() {
        return graphdb_vertex;
    }

    public void setGraphdb_vertex(graphdb_Vertex graphdb_vertex) {
        this.graphdb_vertex = graphdb_vertex;
    }
    public List<graphdb_Vertex> getGraphdb_vertexs() {
        return graphdb_vertexs;
    }

    public void addGraphdb_vertex(Graphdb_vertex graphdb_vertex) {
        this.graphdb_vertexs.add(graphdb_vertex);
    }
    public graphdb_Edge getGraphdb_edge() {
        return graphdb_edge;
    }

    public void setGraphdb_edge(graphdb_Edge graphdb_edge) {
        this.graphdb_edge = graphdb_edge;
    }
    public List<graphdb_Edge> getGraphdb_edges() {
        return graphdb_edges;
    }

    public void addGraphdb_edge(Graphdb_edge graphdb_edge) {
        this.graphdb_edges.add(graphdb_edge);
    }

}