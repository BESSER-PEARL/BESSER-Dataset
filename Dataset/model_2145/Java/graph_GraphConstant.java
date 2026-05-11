





import java.util.List;
import java.util.ArrayList;

public class graph_GraphConstant extends Expr {






    private List<graph_Edge> graph_edges;




    private List<graph_Vertex> graph_vertexs;


    public graph_GraphConstant(
    ) {
        super(
        );
        this.graph_edges = new ArrayList<>();
        this.graph_vertexs = new ArrayList<>();
    }

    public graph_GraphConstant(
        ArrayList<graph_Edge> graph_edges,        ArrayList<graph_Vertex> graph_vertexs    ) {
        this.graph_edges = graph_edges;
        this.graph_vertexs = graph_vertexs;
    }


    public List<graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }
    public List<graph_Vertex> getGraph_vertexs() {
        return graph_vertexs;
    }

    public void addGraph_vertex(Graph_vertex graph_vertex) {
        this.graph_vertexs.add(graph_vertex);
    }

}