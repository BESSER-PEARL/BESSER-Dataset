





import java.util.List;
import java.util.ArrayList;

public class jgrapht_Edge  {

    private String relation;





    private jgrapht_Graph jgrapht_graph;


    public jgrapht_Edge(
        String relation    ) {
        this.relation = relation;
    }


    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }

    public jgrapht_Graph getJgrapht_graph() {
        return jgrapht_graph;
    }

    public void setJgrapht_graph(jgrapht_Graph jgrapht_graph) {
        this.jgrapht_graph = jgrapht_graph;
    }

}