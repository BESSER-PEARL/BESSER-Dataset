





import java.util.List;
import java.util.ArrayList;

public class operators_ResourceExpansion extends Base {






    private List<operators_Equipment> operators_equipments;




    private List<operators_Function> operators_functions;


    public operators_ResourceExpansion(
    ) {
        super(
        );
        this.operators_equipments = new ArrayList<>();
        this.operators_functions = new ArrayList<>();
    }

    public operators_ResourceExpansion(
        ArrayList<operators_Equipment> operators_equipments,        ArrayList<operators_Function> operators_functions    ) {
        this.operators_equipments = operators_equipments;
        this.operators_functions = operators_functions;
    }


    public List<operators_Equipment> getOperators_equipments() {
        return operators_equipments;
    }

    public void addOperators_equipment(Operators_equipment operators_equipment) {
        this.operators_equipments.add(operators_equipment);
    }
    public List<operators_Function> getOperators_functions() {
        return operators_functions;
    }

    public void addOperators_function(Operators_function operators_function) {
        this.operators_functions.add(operators_function);
    }

}