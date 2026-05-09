





import java.util.List;
import java.util.ArrayList;

public class ast_TryStatement extends Statement {






    private List<ast_CatchClause> ast_catchclauses;




    private List<ast_VariableDeclarationExpression> ast_variabledeclarationexpressions;




    private ast_Block ast_block;




    private ast_Block ast_block;


    public ast_TryStatement(
    ) {
        super(
        );
        this.ast_catchclauses = new ArrayList<>();
        this.ast_variabledeclarationexpressions = new ArrayList<>();
    }

    public ast_TryStatement(
        ArrayList<ast_CatchClause> ast_catchclauses,        ArrayList<ast_VariableDeclarationExpression> ast_variabledeclarationexpressions    ) {
        this.ast_catchclauses = ast_catchclauses;
        this.ast_variabledeclarationexpressions = ast_variabledeclarationexpressions;
    }


    public List<ast_CatchClause> getAst_catchclauses() {
        return ast_catchclauses;
    }

    public void addAst_catchclause(Ast_catchclause ast_catchclause) {
        this.ast_catchclauses.add(ast_catchclause);
    }
    public List<ast_VariableDeclarationExpression> getAst_variabledeclarationexpressions() {
        return ast_variabledeclarationexpressions;
    }

    public void addAst_variabledeclarationexpression(Ast_variabledeclarationexpression ast_variabledeclarationexpression) {
        this.ast_variabledeclarationexpressions.add(ast_variabledeclarationexpression);
    }
    public ast_Block getAst_block() {
        return ast_block;
    }

    public void setAst_block(ast_Block ast_block) {
        this.ast_block = ast_block;
    }
    public ast_Block getAst_block() {
        return ast_block;
    }

    public void setAst_block(ast_Block ast_block) {
        this.ast_block = ast_block;
    }

}