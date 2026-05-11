





import java.util.List;
import java.util.ArrayList;

public class types_TypedElement  {






    private List<types_Type> types_types;




    private types_Type types_type;


    public types_TypedElement(
    ) {
        this.types_types = new ArrayList<>();
    }

    public types_TypedElement(
        ArrayList<types_Type> types_types    ) {
        this.types_types = types_types;
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