





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_EnumDeclaration extends AbstractTypeDeclaration {






    private List<Type> types;


    public JavaAbstractSyntax_EnumDeclaration(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public JavaAbstractSyntax_EnumDeclaration(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}