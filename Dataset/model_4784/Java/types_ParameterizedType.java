





import java.util.List;
import java.util.ArrayList;

public class types_ParameterizedType extends Type {






    private List<types_TypeParameter> types_typeparameters;


    public types_ParameterizedType(
    ) {
        super(
        );
        this.types_typeparameters = new ArrayList<>();
    }

    public types_ParameterizedType(
        ArrayList<types_TypeParameter> types_typeparameters    ) {
        this.types_typeparameters = types_typeparameters;
    }


    public List<types_TypeParameter> getTypes_typeparameters() {
        return types_typeparameters;
    }

    public void addTypes_typeparameter(Types_typeparameter types_typeparameter) {
        this.types_typeparameters.add(types_typeparameter);
    }

}