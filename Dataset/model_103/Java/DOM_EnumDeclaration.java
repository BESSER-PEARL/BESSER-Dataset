





import java.util.List;
import java.util.ArrayList;

public class DOM_EnumDeclaration extends AbstractTypeDeclaration {






    private List<Type> types;


    public DOM_EnumDeclaration(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public DOM_EnumDeclaration(
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