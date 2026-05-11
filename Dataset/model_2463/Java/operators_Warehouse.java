





import java.util.List;
import java.util.ArrayList;

public class operators_Warehouse  {

    private String equipments;
    private String description;
    private String name;





    private List<operators_Node> operators_nodes;




    private operators_Operator operators_operator;


    public operators_Warehouse(
        String equipments,        String description,        String name    ) {
        this.equipments = equipments;
        this.description = description;
        this.name = name;
        this.operators_nodes = new ArrayList<>();
    }

    public operators_Warehouse(
        String equipments,        String description,        String name        ArrayList<operators_Node> operators_nodes    ) {
        this.equipments = equipments;
        this.description = description;
        this.name = name;
        this.operators_nodes = operators_nodes;
    }

    public String getEquipments() {
        return equipments;
    }

    public void setEquipments(String equipments) {
        this.equipments = equipments;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<operators_Node> getOperators_nodes() {
        return operators_nodes;
    }

    public void addOperators_node(Operators_node operators_node) {
        this.operators_nodes.add(operators_node);
    }
    public operators_Operator getOperators_operator() {
        return operators_operator;
    }

    public void setOperators_operator(operators_Operator operators_operator) {
        this.operators_operator = operators_operator;
    }

}