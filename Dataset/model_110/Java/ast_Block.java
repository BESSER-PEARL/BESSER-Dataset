





import java.util.List;
import java.util.ArrayList;

public class ast_Block extends Statement {






    private List<ast_Statement> ast_statements;




    private ast_CatchClause ast_catchclause;


    public ast_Block(
    ) {
        super(
        );
        this.ast_statements = new ArrayList<>();
    }

    public ast_Block(
        ArrayList<ast_Statement> ast_statements    ) {
        this.ast_statements = ast_statements;
    }


    public List<ast_Statement> getAst_statements() {
        return ast_statements;
    }

    public void addAst_statement(Ast_statement ast_statement) {
        this.ast_statements.add(ast_statement);
    }
    public ast_CatchClause getAst_catchclause() {
        return ast_catchclause;
    }

    public void setAst_catchclause(ast_CatchClause ast_catchclause) {
        this.ast_catchclause = ast_catchclause;
    }

}