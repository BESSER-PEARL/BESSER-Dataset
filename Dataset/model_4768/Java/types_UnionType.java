





import java.util.List;
import java.util.ArrayList;

public class types_UnionType extends Type {






    private List<types_Type> types_types;


    public types_UnionType(
    ) {
        super(
        );
        this.types_types = new ArrayList<>();
    }

    public types_UnionType(
        ArrayList<types_Type> types_types    ) {
        this.types_types = types_types;
    }


    public List<types_Type> getTypes_types() {
        return types_types;
    }

    public void addTypes_type(Types_type types_type) {
        this.types_types.add(types_type);
    }

}