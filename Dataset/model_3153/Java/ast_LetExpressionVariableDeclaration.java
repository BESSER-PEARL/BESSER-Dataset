





import java.util.List;
import java.util.ArrayList;

public class ast_LetExpressionVariableDeclaration  {






    private ast_LetExpression ast_letexpression;




    private ast_Expression ast_expression;




    private List<ast_LetExpressionVariableDeclarationPart> ast_letexpressionvariabledeclarationparts;


    public ast_LetExpressionVariableDeclaration(
    ) {
        this.ast_letexpressionvariabledeclarationparts = new ArrayList<>();
    }

    public ast_LetExpressionVariableDeclaration(
        ArrayList<ast_LetExpressionVariableDeclarationPart> ast_letexpressionvariabledeclarationparts    ) {
        this.ast_letexpressionvariabledeclarationparts = ast_letexpressionvariabledeclarationparts;
    }


    public ast_LetExpression getAst_letexpression() {
        return ast_letexpression;
    }

    public void setAst_letexpression(ast_LetExpression ast_letexpression) {
        this.ast_letexpression = ast_letexpression;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_LetExpressionVariableDeclarationPart> getAst_letexpressionvariabledeclarationparts() {
        return ast_letexpressionvariabledeclarationparts;
    }

    public void addAst_letexpressionvariabledeclarationpart(Ast_letexpressionvariabledeclarationpart ast_letexpressionvariabledeclarationpart) {
        this.ast_letexpressionvariabledeclarationparts.add(ast_letexpressionvariabledeclarationpart);
    }

}