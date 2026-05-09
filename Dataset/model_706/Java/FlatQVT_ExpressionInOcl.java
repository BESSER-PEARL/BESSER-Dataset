





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_ExpressionInOcl extends TypedElement {






    private OclExpression oclexpression;




    private List<Type> types;


    public FlatQVT_ExpressionInOcl(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public FlatQVT_ExpressionInOcl(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}