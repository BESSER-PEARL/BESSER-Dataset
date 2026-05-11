





import java.util.List;
import java.util.ArrayList;

public class operators_ResourceExpansion extends Base {






    private List<operators_Node> operators_nodes;


    public operators_ResourceExpansion(
    ) {
        super(
        );
        this.operators_nodes = new ArrayList<>();
    }

    public operators_ResourceExpansion(
        ArrayList<operators_Node> operators_nodes    ) {
        this.operators_nodes = operators_nodes;
    }


    public List<operators_Node> getOperators_nodes() {
        return operators_nodes;
    }

    public void addOperators_node(Operators_node operators_node) {
        this.operators_nodes.add(operators_node);
    }

}