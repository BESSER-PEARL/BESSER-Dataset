





import java.util.List;
import java.util.ArrayList;

public class GraphConstraint_NestedGraphConstraint  {

    private String name;





    private GraphConstraint_Graph graphconstraint_graph;


    public GraphConstraint_NestedGraphConstraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public GraphConstraint_Graph getGraphconstraint_graph() {
        return graphconstraint_graph;
    }

    public void setGraphconstraint_graph(GraphConstraint_Graph graphconstraint_graph) {
        this.graphconstraint_graph = graphconstraint_graph;
    }

}