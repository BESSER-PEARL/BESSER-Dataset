





import java.util.List;
import java.util.ArrayList;

public class ast_ExpressionStatement extends MethodContentStatement {






    private ast_Expression ast_expression;


    public ast_ExpressionStatement(
    ) {
        super(
        );
    }



    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}