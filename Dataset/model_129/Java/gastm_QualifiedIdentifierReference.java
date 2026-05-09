





import java.util.List;
import java.util.ArrayList;

public class gastm_QualifiedIdentifierReference extends NameReference {






    private IdentifierReference identifierreference;




    private Expression expression;


    public gastm_QualifiedIdentifierReference(
    ) {
        super(
        );
    }



    public IdentifierReference getIdentifierreference() {
        return identifierreference;
    }

    public void setIdentifierreference(IdentifierReference identifierreference) {
        this.identifierreference = identifierreference;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}