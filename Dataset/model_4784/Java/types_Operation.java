





import java.util.List;
import java.util.ArrayList;

public class types_Operation extends Feature {






    private types_Parameter types_parameter;




    private List<types_Parameter> types_parameters;


    public types_Operation(
    ) {
        super(
        );
        this.types_parameters = new ArrayList<>();
    }

    public types_Operation(
        ArrayList<types_Parameter> types_parameters    ) {
        this.types_parameters = types_parameters;
    }


    public types_Parameter getTypes_parameter() {
        return types_parameter;
    }

    public void setTypes_parameter(types_Parameter types_parameter) {
        this.types_parameter = types_parameter;
    }
    public List<types_Parameter> getTypes_parameters() {
        return types_parameters;
    }

    public void addTypes_parameter(Types_parameter types_parameter) {
        this.types_parameters.add(types_parameter);
    }

}