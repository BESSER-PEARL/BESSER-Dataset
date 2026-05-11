





import java.util.List;
import java.util.ArrayList;

public class graphdb_Vertex extends GraphElement {

    private String name;
    private String labels;





    private graphdb_Edge graphdb_edge;




    private List<graphdb_Edge> graphdb_edges;




    private graphdb_Edge graphdb_edge;




    private List<graphdb_Edge> graphdb_edges;


    public graphdb_Vertex(
        String name,        String labels    ) {
        super(
        );
        this.name = name;
        this.labels = labels;
        this.graphdb_edges = new ArrayList<>();
        this.graphdb_edges = new ArrayList<>();
    }

    public graphdb_Vertex(
        String name,        String labels        ArrayList<graphdb_Edge> graphdb_edges,        ArrayList<graphdb_Edge> graphdb_edges    ) {
        this.name = name;
        this.labels = labels;
        this.graphdb_edges = graphdb_edges;
        this.graphdb_edges = graphdb_edges;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabels() {
        return labels;
    }

    public void setLabels(String labels) {
        this.labels = labels;
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