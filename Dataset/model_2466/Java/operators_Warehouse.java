





import java.util.List;
import java.util.ArrayList;

public class operators_Warehouse extends Base {

    private String description;
    private String name;





    private List<operators_Equipment> operators_equipments;


    public operators_Warehouse(
        String description,        String name    ) {
        super(
        );
        this.description = description;
        this.name = name;
        this.operators_equipments = new ArrayList<>();
    }

    public operators_Warehouse(
        String description,        String name        ArrayList<operators_Equipment> operators_equipments    ) {
        this.description = description;
        this.name = name;
        this.operators_equipments = operators_equipments;
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

    public List<operators_Equipment> getOperators_equipments() {
        return operators_equipments;
    }

    public void addOperators_equipment(Operators_equipment operators_equipment) {
        this.operators_equipments.add(operators_equipment);
    }

}