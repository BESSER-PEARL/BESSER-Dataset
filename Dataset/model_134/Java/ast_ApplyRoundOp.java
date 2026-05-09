





import java.util.List;
import java.util.ArrayList;

public class ast_ApplyRoundOp extends Expression {






    private List<ast_Expression> ast_expressions;




    private ast_Expression ast_expression;


    public ast_ApplyRoundOp(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
    }

    public ast_ApplyRoundOp(
        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
    }


    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}