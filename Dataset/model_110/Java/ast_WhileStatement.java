





import java.util.List;
import java.util.ArrayList;

public class ast_WhileStatement extends Statement {






    private ast_Expression ast_expression;




    private ast_Statement ast_statement;


    public ast_WhileStatement(
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
    public ast_Statement getAst_statement() {
        return ast_statement;
    }

    public void setAst_statement(ast_Statement ast_statement) {
        this.ast_statement = ast_statement;
    }

}