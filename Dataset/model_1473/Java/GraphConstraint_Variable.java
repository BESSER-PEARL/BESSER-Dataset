





import java.util.List;
import java.util.ArrayList;

public class GraphConstraint_Variable  {

    private String name;





    private GraphConstraint_NestedGraphCondition graphconstraint_nestedgraphcondition;


    public GraphConstraint_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public GraphConstraint_NestedGraphCondition getGraphconstraint_nestedgraphcondition() {
        return graphconstraint_nestedgraphcondition;
    }

    public void setGraphconstraint_nestedgraphcondition(GraphConstraint_NestedGraphCondition graphconstraint_nestedgraphcondition) {
        this.graphconstraint_nestedgraphcondition = graphconstraint_nestedgraphcondition;
    }

}