





import java.util.List;
import java.util.ArrayList;

public class types_Operation extends TypedDeclaration, GenericElement {

    private boolean variadic;





    private types_Parameter types_parameter;




    private List<types_Parameter> types_parameters;


    public types_Operation(
        boolean variadic    ) {
        super(
        );
        this.variadic = variadic;
        this.types_parameters = new ArrayList<>();
    }

    public types_Operation(
        boolean variadic        ArrayList<types_Parameter> types_parameters    ) {
        this.variadic = variadic;
        this.types_parameters = types_parameters;
    }

    public boolean getVariadic() {
        return variadic;
    }

    public void setVariadic(boolean variadic) {
        this.variadic = variadic;
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