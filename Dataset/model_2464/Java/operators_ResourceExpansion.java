





import java.util.List;
import java.util.ArrayList;

public class operators_ResourceExpansion  {






    private List<operators_Equipment> operators_equipments;




    private operators_Operator operators_operator;




    private List<operators_Node> operators_nodes;




    private List<operators_Function> operators_functions;


    public operators_ResourceExpansion(
    ) {
        this.operators_equipments = new ArrayList<>();
        this.operators_nodes = new ArrayList<>();
        this.operators_functions = new ArrayList<>();
    }

    public operators_ResourceExpansion(
        ArrayList<operators_Equipment> operators_equipments,        ArrayList<operators_Node> operators_nodes,        ArrayList<operators_Function> operators_functions    ) {
        this.operators_equipments = operators_equipments;
        this.operators_nodes = operators_nodes;
        this.operators_functions = operators_functions;
    }


    public List<operators_Equipment> getOperators_equipments() {
        return operators_equipments;
    }

    public void addOperators_equipment(Operators_equipment operators_equipment) {
        this.operators_equipments.add(operators_equipment);
    }
    public operators_Operator getOperators_operator() {
        return operators_operator;
    }

    public void setOperators_operator(operators_Operator operators_operator) {
        this.operators_operator = operators_operator;
    }
    public List<operators_Node> getOperators_nodes() {
        return operators_nodes;
    }

    public void addOperators_node(Operators_node operators_node) {
        this.operators_nodes.add(operators_node);
    }
    public List<operators_Function> getOperators_functions() {
        return operators_functions;
    }

    public void addOperators_function(Operators_function operators_function) {
        this.operators_functions.add(operators_function);
    }

}