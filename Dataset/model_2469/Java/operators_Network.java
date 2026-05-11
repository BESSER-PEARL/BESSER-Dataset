





import java.util.List;
import java.util.ArrayList;

public class operators_Network extends Base {

    private String createdDate;
    private String name;
    private String description;





    private List<operators_Node> operators_nodes;




    private operators_Network operators_network;




    private List<operators_FunctionRelationship> operators_functionrelationships;




    private List<operators_EquipmentRelationship> operators_equipmentrelationships;


    public operators_Network(
        String createdDate,        String name,        String description    ) {
        super(
        );
        this.createdDate = createdDate;
        this.name = name;
        this.description = description;
        this.operators_nodes = new ArrayList<>();
        this.operators_functionrelationships = new ArrayList<>();
        this.operators_equipmentrelationships = new ArrayList<>();
    }

    public operators_Network(
        String createdDate,        String name,        String description        ArrayList<operators_Node> operators_nodes,        ArrayList<operators_FunctionRelationship> operators_functionrelationships,        ArrayList<operators_EquipmentRelationship> operators_equipmentrelationships    ) {
        this.createdDate = createdDate;
        this.name = name;
        this.description = description;
        this.operators_nodes = operators_nodes;
        this.operators_functionrelationships = operators_functionrelationships;
        this.operators_equipmentrelationships = operators_equipmentrelationships;
    }

    public String getCreateddate() {
        return createdDate;
    }

    public void setCreateddate(String createdDate) {
        this.createdDate = createdDate;
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

    public List<operators_Node> getOperators_nodes() {
        return operators_nodes;
    }

    public void addOperators_node(Operators_node operators_node) {
        this.operators_nodes.add(operators_node);
    }
    public operators_Network getOperators_network() {
        return operators_network;
    }

    public void setOperators_network(operators_Network operators_network) {
        this.operators_network = operators_network;
    }
    public List<operators_FunctionRelationship> getOperators_functionrelationships() {
        return operators_functionrelationships;
    }

    public void addOperators_functionrelationship(Operators_functionrelationship operators_functionrelationship) {
        this.operators_functionrelationships.add(operators_functionrelationship);
    }
    public List<operators_EquipmentRelationship> getOperators_equipmentrelationships() {
        return operators_equipmentrelationships;
    }

    public void addOperators_equipmentrelationship(Operators_equipmentrelationship operators_equipmentrelationship) {
        this.operators_equipmentrelationships.add(operators_equipmentrelationship);
    }

}