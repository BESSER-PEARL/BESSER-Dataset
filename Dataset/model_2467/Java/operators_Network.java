





import java.util.List;
import java.util.ArrayList;

public class operators_Network extends Base {

    private String name;
    private String createdDate;
    private String description;





    private List<operators_FunctionRelationship> operators_functionrelationships;




    private List<operators_EquipmentRelationship> operators_equipmentrelationships;




    private operators_Network operators_network;


    public operators_Network(
        String name,        String createdDate,        String description    ) {
        super(
        );
        this.name = name;
        this.createdDate = createdDate;
        this.description = description;
        this.operators_functionrelationships = new ArrayList<>();
        this.operators_equipmentrelationships = new ArrayList<>();
    }

    public operators_Network(
        String name,        String createdDate,        String description        ArrayList<operators_FunctionRelationship> operators_functionrelationships,        ArrayList<operators_EquipmentRelationship> operators_equipmentrelationships    ) {
        this.name = name;
        this.createdDate = createdDate;
        this.description = description;
        this.operators_functionrelationships = operators_functionrelationships;
        this.operators_equipmentrelationships = operators_equipmentrelationships;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public operators_Network getOperators_network() {
        return operators_network;
    }

    public void setOperators_network(operators_Network operators_network) {
        this.operators_network = operators_network;
    }

}