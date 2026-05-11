





import java.util.List;
import java.util.ArrayList;

public class graphdb_Vertex extends GraphElement {

    private String labels;
    private String name;





    private graphdb_Graph graphdb_graph;




    private graphdb_Graph graphdb_graph;


    public graphdb_Vertex(
        String labels,        String name    ) {
        super(
        );
        this.labels = labels;
        this.name = name;
    }


    public String getLabels() {
        return labels;
    }

    public void setLabels(String labels) {
        this.labels = labels;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphdb_Graph getGraphdb_graph() {
        return graphdb_graph;
    }

    public void setGraphdb_graph(graphdb_Graph graphdb_graph) {
        this.graphdb_graph = graphdb_graph;
    }
    public graphdb_Graph getGraphdb_graph() {
        return graphdb_graph;
    }

    public void setGraphdb_graph(graphdb_Graph graphdb_graph) {
        this.graphdb_graph = graphdb_graph;
    }

}