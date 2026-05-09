





import java.util.List;
import java.util.ArrayList;

public class GraphConstraint_Attribute extends GraphElement {

    private String op;
    private String value;





    private GraphConstraint_Node graphconstraint_node;




    private GraphConstraint_EAttribute graphconstraint_eattribute;


    public GraphConstraint_Attribute(
        String op,        String value    ) {
        super(
        );
        this.op = op;
        this.value = value;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public GraphConstraint_Node getGraphconstraint_node() {
        return graphconstraint_node;
    }

    public void setGraphconstraint_node(GraphConstraint_Node graphconstraint_node) {
        this.graphconstraint_node = graphconstraint_node;
    }
    public GraphConstraint_EAttribute getGraphconstraint_eattribute() {
        return graphconstraint_eattribute;
    }

    public void setGraphconstraint_eattribute(GraphConstraint_EAttribute graphconstraint_eattribute) {
        this.graphconstraint_eattribute = graphconstraint_eattribute;
    }

}