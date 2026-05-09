





import java.util.List;
import java.util.ArrayList;

public class GraphConstraint_Formula extends NestedGraphCondition {

    private String op;





    private GraphConstraint_NestedGraphCondition graphconstraint_nestedgraphcondition;




    private List<GraphConstraint_NestedGraphCondition> graphconstraint_nestedgraphconditions;


    public GraphConstraint_Formula(
        String op    ) {
        super(
        );
        this.op = op;
        this.graphconstraint_nestedgraphconditions = new ArrayList<>();
    }

    public GraphConstraint_Formula(
        String op        ArrayList<GraphConstraint_NestedGraphCondition> graphconstraint_nestedgraphconditions    ) {
        this.op = op;
        this.graphconstraint_nestedgraphconditions = graphconstraint_nestedgraphconditions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public GraphConstraint_NestedGraphCondition getGraphconstraint_nestedgraphcondition() {
        return graphconstraint_nestedgraphcondition;
    }

    public void setGraphconstraint_nestedgraphcondition(GraphConstraint_NestedGraphCondition graphconstraint_nestedgraphcondition) {
        this.graphconstraint_nestedgraphcondition = graphconstraint_nestedgraphcondition;
    }
    public List<GraphConstraint_NestedGraphCondition> getGraphconstraint_nestedgraphconditions() {
        return graphconstraint_nestedgraphconditions;
    }

    public void addGraphconstraint_nestedgraphcondition(Graphconstraint_nestedgraphcondition graphconstraint_nestedgraphcondition) {
        this.graphconstraint_nestedgraphconditions.add(graphconstraint_nestedgraphcondition);
    }

}