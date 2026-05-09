





import java.util.List;
import java.util.ArrayList;

public class ast_VariableDeclaration extends ASTNode {






    private ast_LambdaExpression ast_lambdaexpression;


    public ast_VariableDeclaration(
    ) {
        super(
        );
    }



    public ast_LambdaExpression getAst_lambdaexpression() {
        return ast_lambdaexpression;
    }

    public void setAst_lambdaexpression(ast_LambdaExpression ast_lambdaexpression) {
        this.ast_lambdaexpression = ast_lambdaexpression;
    }

}