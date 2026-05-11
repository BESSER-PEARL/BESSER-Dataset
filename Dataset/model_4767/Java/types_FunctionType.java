





import java.util.List;
import java.util.ArrayList;

public class types_FunctionType extends Type {

    private int optionalParameterCount;





    private List<types_Type> types_types;




    private types_Type types_type;


    public types_FunctionType(
        int optionalParameterCount    ) {
        super(
        );
        this.optionalParameterCount = optionalParameterCount;
        this.types_types = new ArrayList<>();
    }

    public types_FunctionType(
        int optionalParameterCount        ArrayList<types_Type> types_types    ) {
        this.optionalParameterCount = optionalParameterCount;
        this.types_types = types_types;
    }

    public int getOptionalparametercount() {
        return optionalParameterCount;
    }

    public void setOptionalparametercount(int optionalParameterCount) {
        this.optionalParameterCount = optionalParameterCount;
    }

    public List<types_Type> getTypes_types() {
        return types_types;
    }

    public void addTypes_type(Types_type types_type) {
        this.types_types.add(types_type);
    }
    public types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(types_Type types_type) {
        this.types_type = types_type;
    }

}