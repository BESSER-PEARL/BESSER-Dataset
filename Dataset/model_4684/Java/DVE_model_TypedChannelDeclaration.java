





import java.util.List;
import java.util.ArrayList;

public class DVE_model_TypedChannelDeclaration extends ChannelDeclaration {






    private List<Type> types;




    private Expression expression;


    public DVE_model_TypedChannelDeclaration(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public DVE_model_TypedChannelDeclaration(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}