





import java.util.List;
import java.util.ArrayList;

public class ast_ApplySquareOp extends Expression {






    private ast_Expression ast_expression;




    private List<ast_Expression> ast_expressions;


    public ast_ApplySquareOp(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
    }

    public ast_ApplySquareOp(
        ArrayList<ast_Expression> ast_expressions    ) {
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

}