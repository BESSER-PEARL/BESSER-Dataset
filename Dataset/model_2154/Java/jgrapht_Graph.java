





import java.util.List;
import java.util.ArrayList;

public class jgrapht_Graph  {






    private List<jgrapht_Vertex> jgrapht_vertexs;




    private List<jgrapht_Edge> jgrapht_edges;


    public jgrapht_Graph(
    ) {
        this.jgrapht_vertexs = new ArrayList<>();
        this.jgrapht_edges = new ArrayList<>();
    }

    public jgrapht_Graph(
        ArrayList<jgrapht_Vertex> jgrapht_vertexs,        ArrayList<jgrapht_Edge> jgrapht_edges    ) {
        this.jgrapht_vertexs = jgrapht_vertexs;
        this.jgrapht_edges = jgrapht_edges;
    }


    public List<jgrapht_Vertex> getJgrapht_vertexs() {
        return jgrapht_vertexs;
    }

    public void addJgrapht_vertex(Jgrapht_vertex jgrapht_vertex) {
        this.jgrapht_vertexs.add(jgrapht_vertex);
    }
    public List<jgrapht_Edge> getJgrapht_edges() {
        return jgrapht_edges;
    }

    public void addJgrapht_edge(Jgrapht_edge jgrapht_edge) {
        this.jgrapht_edges.add(jgrapht_edge);
    }

}