





import java.util.List;
import java.util.ArrayList;

public class vml_Edge extends DiagramElement {

    private String relation;





    private vml_Graph vml_graph;


    public vml_Edge(
        String relation    ) {
        super(
        );
        this.relation = relation;
    }


    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }

    public vml_Graph getVml_graph() {
        return vml_graph;
    }

    public void setVml_graph(vml_Graph vml_graph) {
        this.vml_graph = vml_graph;
    }

}