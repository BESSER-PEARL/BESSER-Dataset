





import java.util.List;
import java.util.ArrayList;

public class operators_Warehouse extends Base {

    private String name;
    private String description;





    private List<operators_Equipment> operators_equipments;




    private List<operators_Node> operators_nodes;


    public operators_Warehouse(
        String name,        String description    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.operators_equipments = new ArrayList<>();
        this.operators_nodes = new ArrayList<>();
    }

    public operators_Warehouse(
        String name,        String description        ArrayList<operators_Equipment> operators_equipments,        ArrayList<operators_Node> operators_nodes    ) {
        this.name = name;
        this.description = description;
        this.operators_equipments = operators_equipments;
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

    public List<operators_Equipment> getOperators_equipments() {
        return operators_equipments;
    }

    public void addOperators_equipment(Operators_equipment operators_equipment) {
        this.operators_equipments.add(operators_equipment);
    }
    public List<operators_Node> getOperators_nodes() {
        return operators_nodes;
    }

    public void addOperators_node(Operators_node operators_node) {
        this.operators_nodes.add(operators_node);
    }

}