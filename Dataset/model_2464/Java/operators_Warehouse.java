





import java.util.List;
import java.util.ArrayList;

public class operators_Warehouse  {

    private String name;
    private String description;
    private String equipments;





    private operators_Operator operators_operator;




    private List<operators_Node> operators_nodes;


    public operators_Warehouse(
        String name,        String description,        String equipments    ) {
        this.name = name;
        this.description = description;
        this.equipments = equipments;
        this.operators_nodes = new ArrayList<>();
    }

    public operators_Warehouse(
        String name,        String description,        String equipments        ArrayList<operators_Node> operators_nodes    ) {
        this.name = name;
        this.description = description;
        this.equipments = equipments;
        this.operators_nodes = operators_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getEquipments() {
        return equipments;
    }

    public void setEquipments(String equipments) {
        this.equipments = equipments;
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

}