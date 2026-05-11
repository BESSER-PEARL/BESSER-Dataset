





import java.util.List;
import java.util.ArrayList;

public class operators_Network  {

    private String description;
    private String name;
    private String createdDate;





    private List<operators_Network> operators_networks;




    private List<operators_EquipmentRelationship> operators_equipmentrelationships;




    private List<operators_FunctionRelationship> operators_functionrelationships;


    public operators_Network(
        String description,        String name,        String createdDate    ) {
        this.description = description;
        this.name = name;
        this.createdDate = createdDate;
        this.operators_networks = new ArrayList<>();
        this.operators_equipmentrelationships = new ArrayList<>();
        this.operators_functionrelationships = new ArrayList<>();
    }

    public operators_Network(
        String description,        String name,        String createdDate        ArrayList<operators_Network> operators_networks,        ArrayList<operators_EquipmentRelationship> operators_equipmentrelationships,        ArrayList<operators_FunctionRelationship> operators_functionrelationships    ) {
        this.description = description;
        this.name = name;
        this.createdDate = createdDate;
        this.operators_networks = operators_networks;
        this.operators_equipmentrelationships = operators_equipmentrelationships;
        this.operators_functionrelationships = operators_functionrelationships;
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
    public String getCreateddate() {
        return createdDate;
    }

    public void setCreateddate(String createdDate) {
        this.createdDate = createdDate;
    }

    public List<operators_Network> getOperators_networks() {
        return operators_networks;
    }

    public void addOperators_network(Operators_network operators_network) {
        this.operators_networks.add(operators_network);
    }
    public List<operators_EquipmentRelationship> getOperators_equipmentrelationships() {
        return operators_equipmentrelationships;
    }

    public void addOperators_equipmentrelationship(Operators_equipmentrelationship operators_equipmentrelationship) {
        this.operators_equipmentrelationships.add(operators_equipmentrelationship);
    }
    public List<operators_FunctionRelationship> getOperators_functionrelationships() {
        return operators_functionrelationships;
    }

    public void addOperators_functionrelationship(Operators_functionrelationship operators_functionrelationship) {
        this.operators_functionrelationships.add(operators_functionrelationship);
    }

}