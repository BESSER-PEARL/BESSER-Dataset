





import java.util.List;
import java.util.ArrayList;

public class c_sharp_expressions_BaseAccess extends PrimaryNoArrayCreationExpression {






    private ExpressionList expressionlist;




    private Identifier identifier;


    public c_sharp_expressions_BaseAccess(
    ) {
        super(
        );
    }



    public ExpressionList getExpressionlist() {
        return expressionlist;
    }

    public void setExpressionlist(ExpressionList expressionlist) {
        this.expressionlist = expressionlist;
    }
    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }

}