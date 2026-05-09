





import java.util.List;
import java.util.ArrayList;

public class EssentialOCL_ExpressionInOcl extends TypedElement {






    private List<Type> types;


    public EssentialOCL_ExpressionInOcl(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public EssentialOCL_ExpressionInOcl(
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