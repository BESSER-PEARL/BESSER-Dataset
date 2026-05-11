





import java.util.List;
import java.util.ArrayList;

public class types_ComplexType extends Type, GenericElement {






    private List<types_Declaration> types_declarations;


    public types_ComplexType(
    ) {
        super(
        );
        this.types_declarations = new ArrayList<>();
    }

    public types_ComplexType(
        ArrayList<types_Declaration> types_declarations    ) {
        this.types_declarations = types_declarations;
    }


    public List<types_Declaration> getTypes_declarations() {
        return types_declarations;
    }

    public void addTypes_declaration(Types_declaration types_declaration) {
        this.types_declarations.add(types_declaration);
    }

}