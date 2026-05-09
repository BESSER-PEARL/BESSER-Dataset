





import java.util.List;
import java.util.ArrayList;

public class ast_SwitchStatement extends Statement {






    private ast_Expression ast_expression;




    private List<ast_Statement> ast_statements;


    public ast_SwitchStatement(
    ) {
        super(
        );
        this.ast_statements = new ArrayList<>();
    }

    public ast_SwitchStatement(
        ArrayList<ast_Statement> ast_statements    ) {
        this.ast_statements = ast_statements;
    }


    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_Statement> getAst_statements() {
        return ast_statements;
    }

    public void addAst_statement(Ast_statement ast_statement) {
        this.ast_statements.add(ast_statement);
    }

}