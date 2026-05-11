





import java.util.List;
import java.util.ArrayList;

public class types_ComplexType extends ParameterizedType {






    private List<types_Declaration> types_declarations;




    private List<types_ComplexType> types_complextypes;


    public types_ComplexType(
    ) {
        super(
        );
        this.types_declarations = new ArrayList<>();
        this.types_complextypes = new ArrayList<>();
    }

    public types_ComplexType(
        ArrayList<types_Declaration> types_declarations,        ArrayList<types_ComplexType> types_complextypes    ) {
        this.types_declarations = types_declarations;
        this.types_complextypes = types_complextypes;
    }


    public List<types_Declaration> getTypes_declarations() {
        return types_declarations;
    }

    public void addTypes_declaration(Types_declaration types_declaration) {
        this.types_declarations.add(types_declaration);
    }
    public List<types_ComplexType> getTypes_complextypes() {
        return types_complextypes;
    }

    public void addTypes_complextype(Types_complextype types_complextype) {
        this.types_complextypes.add(types_complextype);
    }

}