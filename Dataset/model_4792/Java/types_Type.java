





import java.util.List;
import java.util.ArrayList;

public class types_Type extends NamedElement {






    private types_Library types_library;




    private types_Library types_library;




    private List<types_Type> types_types;


    public types_Type(
    ) {
        super(
        );
        this.types_types = new ArrayList<>();
    }

    public types_Type(
        ArrayList<types_Type> types_types    ) {
        this.types_types = types_types;
    }


    public types_Library getTypes_library() {
        return types_library;
    }

    public void setTypes_library(types_Library types_library) {
        this.types_library = types_library;
    }
    public types_Library getTypes_library() {
        return types_library;
    }

    public void setTypes_library(types_Library types_library) {
        this.types_library = types_library;
    }
    public List<types_Type> getTypes_types() {
        return types_types;
    }

    public void addTypes_type(Types_type types_type) {
        this.types_types.add(types_type);
    }

}