





import java.util.List;
import java.util.ArrayList;

public class ast_ForStatement extends Statement {






    private ast_Expression ast_expression;




    private List<ast_Expression> ast_expressions;




    private List<ast_Expression> ast_expressions;




    private ast_Statement ast_statement;


    public ast_ForStatement(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
        this.ast_expressions = new ArrayList<>();
    }

    public ast_ForStatement(
        ArrayList<ast_Expression> ast_expressions,        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
        this.ast_expressions = ast_expressions;
    }


    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public ast_Statement getAst_statement() {
        return ast_statement;
    }

    public void setAst_statement(ast_Statement ast_statement) {
        this.ast_statement = ast_statement;
    }

}