





import java.util.List;
import java.util.ArrayList;

public class DOM_EnhancedForStatement extends Statement {






    private Expression expression;




    private SingleVariableDeclaration singlevariabledeclaration;


    public DOM_EnhancedForStatement(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public SingleVariableDeclaration getSinglevariabledeclaration() {
        return singlevariabledeclaration;
    }

    public void setSinglevariabledeclaration(SingleVariableDeclaration singlevariabledeclaration) {
        this.singlevariabledeclaration = singlevariabledeclaration;
    }

}