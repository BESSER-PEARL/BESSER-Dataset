





import java.util.List;
import java.util.ArrayList;

public class types_EnumType extends IdlTypeDcl {






    private List<types_Enumeration> types_enumerations;


    public types_EnumType(
    ) {
        super(
        );
        this.types_enumerations = new ArrayList<>();
    }

    public types_EnumType(
        ArrayList<types_Enumeration> types_enumerations    ) {
        this.types_enumerations = types_enumerations;
    }


    public List<types_Enumeration> getTypes_enumerations() {
        return types_enumerations;
    }

    public void addTypes_enumeration(Types_enumeration types_enumeration) {
        this.types_enumerations.add(types_enumeration);
    }

}