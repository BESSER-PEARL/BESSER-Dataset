





import java.util.List;
import java.util.ArrayList;

public class ast_LambdaExpression extends Expression {

    private boolean parentheses;





    private ast_ASTNode ast_astnode;


    public ast_LambdaExpression(
        boolean parentheses    ) {
        super(
        );
        this.parentheses = parentheses;
    }


    public boolean getParentheses() {
        return parentheses;
    }

    public void setParentheses(boolean parentheses) {
        this.parentheses = parentheses;
    }

    public ast_ASTNode getAst_astnode() {
        return ast_astnode;
    }

    public void setAst_astnode(ast_ASTNode ast_astnode) {
        this.ast_astnode = ast_astnode;
    }

}