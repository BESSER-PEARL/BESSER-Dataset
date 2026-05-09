





import java.util.List;
import java.util.ArrayList;

public class DOM_EnhancedForStatement extends Statement {






    private SingleVariableDeclaration singlevariabledeclaration;




    private Expression expression;


    public DOM_EnhancedForStatement(
    ) {
        super(
        );
    }



    public SingleVariableDeclaration getSinglevariabledeclaration() {
        return singlevariabledeclaration;
    }

    public void setSinglevariabledeclaration(SingleVariableDeclaration singlevariabledeclaration) {
        this.singlevariabledeclaration = singlevariabledeclaration;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}